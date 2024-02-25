from django.shortcuts import render
from . models import Blog, BlogSubContent, KeyWord
from django.core.paginator import Paginator

def blog_list(request):
    blog_list = Blog.objects.all().order_by("-blog_date")
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page', 1)
    blogs = paginator.page(page_number)
    return render(request, "Blog/blogs.html", {"blogs" :blogs })

def blog_detail(request, blog_name, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    return render(request, "Blog/blog_detail.html", {"blog" : blog})
