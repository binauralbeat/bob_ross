from .views import *
from django.conf.urls import url
from brjr import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^birthdays$', views.birthday_data, name='not_home'),

]