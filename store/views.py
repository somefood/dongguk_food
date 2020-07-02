from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Store
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MenuInlineFormSet
from mysite.views import AdminOnlyMixin
from django.conf import settings
import json

class StoreIndexView(ListView):
    template_name = 'store/index.html'
    context_object_name = "store_list"

    def get_queryset(self):
        return Store.objects.all()


class CategoryView(ListView):
    template_name = 'store/index.html'
    context_object_name = 'store_list'

    def get_queryset(self):
        return Store.objects.filter(category=self.kwargs['category'])

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
        'nickname': request.user.profile.nickname
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
    # return redirect(store.get_absolute_url())


class StoreDetailView(DetailView):
    model = Store
    template_name = 'store/store_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context


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