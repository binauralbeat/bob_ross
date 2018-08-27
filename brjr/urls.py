from .views import *
from django.conf.urls import url
from brjr import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

]