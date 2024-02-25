from django.urls import path, include
from . views import *

urlpatterns = [
    path('', home , name='home'),
    path('contact/', Contact , name='contact'),
    path('search/', search, name="search"),
    path('subscribe/', subscribe, name="subscribe"),
]