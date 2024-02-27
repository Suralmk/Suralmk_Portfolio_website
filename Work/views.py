from django.shortcuts import render, redirect
from . models import Work, WorkTechnology
from django.template.loader import render_to_string
from PortfolioApp. models import Subscription
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags

def work_list(request):
    works = Work.objects.all()
    return render(request, "Work/works.html", {"works":works})

def work_detail(request, work_name, work_id):
    work = Work.objects.filter(id=work_id).first()

    return render(request, "Work/work_detail.html", {"work" :work})


def work_create(request):
    if not request.user.is_superuser:
        return redirect("blog-list")
    if request.method == "POST":
        try:
            work_title = request.POST["work_title"]
            work_year = request.POST["work_year"]
            work_description = request.POST["work_desc"]
            work_presentation = request.POST["work_presentation"]
            work_challenges = request.POST["work_challenges"]
            project_url = request.POST["project_url"]
            github_url = request.POST["github_url"]
            work_picture = request.FILES["work_picture"]

            work = Work.objects.create(
                work_title=work_title,
                work_year=work_year,
                work_description=work_description,
                work_presentaion=work_presentation,
                work_problems=work_challenges,
                work_project_url=project_url,
                work_github_url=github_url,
                work_picture=work_picture
            )
            work.save()
            # Fetch the blog
            current_site = get_current_site(request)
            subject = "New Project from Surafel Melaku"
            template = render_to_string('Work/work_success.html',
                                        {"work" : work})
            plain_message = strip_tags(template)

            subscribers = Subscription.objects.all()
            recivers = [subscriber.email for subscriber in subscribers]
            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                to=recivers
            )
            email.attach_alternative(template, "text/html")
            email.send()
        except Exception as e:
            print(e)
    return render (request, "Work/work_create.html")