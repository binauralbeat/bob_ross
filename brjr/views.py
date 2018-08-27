from django.shortcuts import render
from .views import *
# Create your views here.

def index(request):
    return render(request, 'brjr/index.html')
