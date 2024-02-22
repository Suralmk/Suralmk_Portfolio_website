from django.urls import path
from . views import *
urlpatterns = [
    path('', work_list, name="work-list"),
    path('<slug:work_name>/<int:work_id>/', work_detail, name="work-detail"),
]