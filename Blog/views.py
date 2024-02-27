from django.shortcuts import render, redirect
from . models import Blog
from django.core.paginator import Paginator
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from PortfolioApp.models import Subscription


def blog_list(request):
    blog_list = Blog.objects.all().order_by("-blog_date")
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page', 1)
    blogs = paginator.page(page_number)
    return render(request, "Blog/blogs.html", {"blogs" :blogs })

def blog_detail(request, blog_name, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    return render(request, "Blog/blog_detail.html", {"blog" : blog})

def blog_create(request):
    if not request.user.is_superuser:
        return redirect("blog-list")
    if request.method == "POST":
        try:
            blog_title = request.POST["blog_title"]
            blog_content = request.POST["blog_content"]
            blog_picture = request.FILES["blog_picture"]

            blog = Blog.objects.create(
                blog_title=blog_title,
                blog_content=blog_content,
                blog_picture=blog_picture
            )
            blog.save()
            # Fetch the blog
            subject = "New Blog from Surafel Melaku"
            template = render_to_string('Blog/email_success.html',
                                        {"blog" : blog, })
            plain_message = strip_tags(template)
            subscribers = Subscription.objects.all()
            recivers = [subscriber.email for subscriber in subscribers]
            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                to=recivers
            )
            email.attach_alternative(template, 'text/html')
            email.send()
        except Exception as e:
            print(e)
    return render(request, "Blog/blog_create.html")
