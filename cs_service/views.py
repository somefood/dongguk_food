from django.shortcuts import render

def index(request):
    return render(request, 'cs_service/index.html')

def terms(request):
    return render(request, 'cs_service/terms.html')

def voice(request):
    return render(request, 'cs_service/voice.html')