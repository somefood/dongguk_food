from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Store

def index(request):
    store = Store.objects.all()
    return render(request, 'food/index.html', {'store': store })

def recom(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'food/recom.html', {'store': store })