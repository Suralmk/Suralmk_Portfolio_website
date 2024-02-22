from django.shortcuts import render
from . models import Work, WorkTechnology

def work_list(request):
    works = Work.objects.all()
    return render(request, "Work/works.html", {"works":works})

def work_detail(request, work_name, work_id):
    work = Work.objects.filter(id=work_id).first()

    return render(request, "Work/work_detail.html", {"work" :work})