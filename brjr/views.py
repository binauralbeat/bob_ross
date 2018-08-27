from django.shortcuts import render
from .views import *
from django.http import JsonResponse
from brjr.models import *
# Create your views here.

def index(request):
    return render(request, 'brjr/index.html')


def birthday_data(request):
    birthdays = Birthday.objects.all().values()
    birthday_list = list(birthdays)

    return JsonResponse(birthday_list, safe=False)
