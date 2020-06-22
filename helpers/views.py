from django.shortcuts import render
from django.views.generic import FormView

from store.models import Store
from board.models import UserBoard

from .forms import SearchForm
from django.db.models import Q
from django.shortcuts import  render

from django.views.generic import ListView, DeleteView, TemplateView

def search_word(request):
    if request.method == "POST":
        print('hi1')
        form = SearchForm(request.POST)
        print('hi2')
        if form.is_valid():
            print('hi3')
            print(request.POST)
            print('hi4')
            q = request.POST.get('q', '검색명을 입력해주세요.')
            print(q)
            if q:
                store_list = Store.objects.filter(Q(name__icontains=q) | Q(description__icontains=q)).distinct()
                board_list = UserBoard.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).distinct()
                return render(request, 'helpers/search_result.html', {'store_list': store_list,
                                                                      'board_list': board_list,
                                                                      'search_word': q})
            else:
                return render(request, 'helpers/search_result.html', {'search_word: q'})
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


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(TemplateView):
    template_name = 'taggit/taggit_post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        store = Store.objects.filter(tags__name=self.kwargs.get('tag'))
        board = UserBoard.objects.filter(tags__name=self.kwargs.get('tag'))

        context['store_list'] = store
        context['board_list'] = board
        context['tagname'] = self.kwargs['tag']
        return context