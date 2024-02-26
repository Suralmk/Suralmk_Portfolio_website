from django.urls import path
from . views import *

urlpatterns = [
    path("", blog_list, name="blog-list"),
    path("<slug:blog_name>/<int:blog_id>/", blog_detail, name="blog-detail"),
    path("blog-create/", blog_create, name="blog-create")
]