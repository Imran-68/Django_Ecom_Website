from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def blog(request):
    return render(request, "blog/index.html")