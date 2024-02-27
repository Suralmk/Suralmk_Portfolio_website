from django.shortcuts import render, redirect
from Blog. models import Blog
from Work . models import Work
from django.db.models import Q
from . forms import SubscriptionForm
from . models import Subscription
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import json
def home(request):
    blogs = Blog.objects.all().order_by("-blog_date")
    works = Work.objects.all()
    context = {
        "blogs":blogs,
        "works":works
    }
    return render(request, "PortfolioApp/home.html", context)

def Contact(request):

    if request.method == "POST":
        try:
            full_name =  request.POST["full_name"]
            contact_email = request.POST["contact_email"]
            message = request.POST["message"]

            subject = "Contact me request"
            body = f" Name: {full_name} \n\n Email: {contact_email} \n\n Message: {message} \n\n"
            
            recivers = [settings.WEBSITE_OWNER]
            email = EmailMessage(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                recivers
            )
            email.fail_silently = False
            email.send()
        except Exception as e:
            print(e)


    return render(request, "PortfolioApp/contact.html")

def search(request):
    query = request.GET["search"]
    blogs = Blog.objects.filter(Q(blog_title__icontains=query))
    return render(request, 'PortfolioApp/search.html', locals())

@require_POST
def subscribe(request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                data = json.load(request)
                email = data.get('email')
                if Subscription.objects.filter(email=email).exists():
                    return JsonResponse({"error" : "You have already subscribed "})
                Subscription.objects.create(email=email)
                return JsonResponse({'success': 'Succesfully Subscribed, Thank you!'})
            return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            return JsonResponse({"statuc" : 'Invalid request'})


