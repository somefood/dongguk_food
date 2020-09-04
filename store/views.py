from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Store
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from .forms import MenuInlineFormSet, CommentForm
from mysite.views import AdminOnlyMixin
from django.conf import settings
import json


class StoreIndexView(ListView):
    template_name = 'store/index.html'
    context_object_name = "store_list"
    paginate_by = 10

    def get_queryset(self):
        return Store.objects.prefetch_related('menu_set').prefetch_related('like_users').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


class CategoryView(ListView):
    template_name = 'store/index.html'
    context_object_name = 'store_list'
    paginate_by = 10

    def get_queryset(self):
        return Store.objects.filter(category=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


@login_required
def like(request):
    pk = request.GET.get('pk', None)
    store = get_object_or_404(Store, pk=pk)

    if request.user in store.like_users.all():
        store.like_users.remove(request.user)
        store.like_count -= 1
        store.save()
        message = False
    else:
        store.like_users.add(request.user)
        store.like_count += 1
        store.save()
        message = True
    context = {
        'like_count': store.like_users.count(),
        'message': message,
        'nickname': request.user.nickname
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
    # return redirect(store.get_absolute_url())


def comment_create(request, slug):
    if not request.user.is_authenticated:
        return JsonResponse({'authenticated': False})
    store = get_object_or_404(Store, slug=slug)
    form = CommentForm(request.POST)
    if form.is_valid():
        form.instance.writer = request.user
        form.instance.store = store
        comment = form.save()
    html = render_to_string('_comment.html', {'comment': comment})
    return JsonResponse({'html': html, 'authenticated': True})


class StoreDetailView(FormMixin, DetailView):
    model = Store
    template_name = 'store/store_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if not request.user.is_authenticated:
            return self.render_to_response(self.get_context_data(form=form))

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.store = get_object_or_404(Store, pk=self.object.pk)
        comment.writer = self.request.user
        comment.save()
        return render(self.request, '_comment.html', {'comment': comment})


class StoreCreateView(AdminOnlyMixin, CreateView):
    model = Store
    fields = ['category', 'name', 'location', 'phone_number', 'description', 'store_image', 'tags', 'running_time']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('store:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = MenuInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = MenuInlineFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class StoreEditView(AdminOnlyMixin, UpdateView):
    model = Store
    fields = ['category', 'name', 'location', 'phone_number', 'description', 'store_image', 'tags', 'running_time']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = MenuInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = MenuInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class StoreDeleteView(AdminOnlyMixin, DeleteView):
    model = Store
    success_url = reverse_lazy('store:index')