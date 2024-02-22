from django.shortcuts import render, redirect
from Blog. models import Blog
from Work . models import Work
from django.db.models import Q
from . forms import SubscriptionForm
from . models import Subscription
from django.contrib import messages
def home(request):
    blogs = Blog.objects.all().order_by("-blog_date")
    works = Work.objects.all()
    if request.method == "POST":
        print("email")
    context = {
        "blogs":blogs,
        "works":works
    }
    return render(request, "PortfolioApp/home.html", context)

def Contact(request):
    if request.method == "POST":
            sub_email = request.POST["sub_email"]
            print(sub_email)
            subscribe = Subscription (
                email=sub_email
            )
            subscribe.save()
            messages.success(request, "Sucesfully Subscribed, Thank you!")
    return render(request, "PortfolioApp/contact.html")

def search(request):
    query = request.GET["search"]
    blogs = Blog.objects.filter(Q(blog_title__icontains=query))
    return render(request, 'PortfolioApp/search.html', locals())

def subscribe(request):
    return redirect("")