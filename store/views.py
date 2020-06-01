from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Store
from django.views.generic import ListView, DetailView

# def index(request):
#     store = Store.objects.all()
#     return render(request, 'store/index.html', {'store': store })
class StoreIndex(ListView):
    template_name = 'store/index.html'
    context_object_name = "store_list"

    def get_queryset(self):
        return Store.objects.all()

def recom(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'store/store_detail.html', {'store': store})

class StoreDetail(DetailView):
    model = Store
    template_name = 'store/store_detail.html'