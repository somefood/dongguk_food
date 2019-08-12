from django.shortcuts import render
from django.http import HttpResponse
from .models import Store

def index(request):
    store = Store.objects.all()
    return render(request, 'food/index.html', {'store': store })
