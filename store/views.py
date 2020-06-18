from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Store
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StoreIndexView(ListView):
    template_name = 'store/index.html'
    context_object_name = "store_list"

    def get_queryset(self):
        return Store.objects.all()


def store_like(request, pk):
    store = get_object_or_404(Store, pk=pk)
    store.likes += 1

class StoreDetailView(DetailView):
    model = Store
    template_name = 'store/store_detail.html'


class StoreCreateView(CreateView):
    model = Store
    fields = '__all__'


class StoreEditView(UpdateView):
    model = Store
    fields = ['name', 'location', 'phone_number', 'description', 'store_image']
    template_name_suffix = '_edit_form'


class StoreDeleteView(DeleteView):
    model = Store
    success_url = reverse_lazy('store:index')