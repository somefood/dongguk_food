from django.shortcuts import render
from django.views.generic import FormView

from store.models import Store
from board.models import UserBoard

from .forms import SearchForm
from django.db.models import Q
from django.shortcuts import  render


def search_word(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        print(form)
        if form.is_valid():
            q = request.POST.get('q', '')
            print(q)
            store_list = Store.objects.filter(Q(name__icontains=q) | Q(description__icontains=q)).distinct()
            board_list = UserBoard.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).distinct()
            return render(request, 'helpers/search_result.html', {'store_list': store_list,
                                                                  'board_list': board_list,
                                                                  'search_word': q})
            # return render(request, 'helpers/search_result', {})


# class SearchFormView(FormView):
#     form_class = SearchForm
#     template_name = 'base.html'
#
#     def form_valid(self, form):
#         searchWord = form.cleaned_data['search_word']
#         post_list = Store.objects.filter(Q(name__icontains=searchWord) | Q(description__icontains=searchWord)).distinct()
#
#         context = {}
#         context['form'] = form
#         context['search_term'] = searchWord
#         context['object_list'] = post_list
#
#         return render(self.request, 'helpers/search_result', context)