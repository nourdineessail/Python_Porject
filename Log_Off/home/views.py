from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request, 'home.html')
def css(request):
    return render(request, 'home1.html')
