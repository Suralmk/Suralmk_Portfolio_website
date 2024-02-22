from django.db import models
from django.utils.text import slugify
# Create your models here.

def work_directory_path(instance, filename):
    print(instance.id)
    return 'work/work_{0}/{1}'.format(instance.id, filename)

class Work(models.Model):
    work_title = models.CharField(max_length=200)
    work_picture = models.ImageField(upload_to=work_directory_path)
    work_year = models.IntegerField()
    work_presentaion = models.TextField(max_length=2000)
    work_problems =models.TextField(max_length=2000)
    work_project_url=models.URLField(blank=True, null=True)
    work_github_url=models.URLField(blank=True, null=True)


    def __str__(self):
        return self.work_title
    
    def get_slug(self):
        return slugify(self.work_title, allow_unicode=True)

class WorkTechnology(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="work_technology")
    tech = models.CharField(max_length=50)

    def __str__(self):
        return self.tech 