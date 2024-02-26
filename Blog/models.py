from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

def blog_directory_path(instance, filename):
    return 'blog/{0}'.format( filename)

class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_picture = models.ImageField(upload_to=blog_directory_path)
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_content = models.TextField(max_length=4000)

    def __str__(self):
        return self.blog_title
    
    def get_slug(self):
        return slugify(self.blog_title, allow_unicode=True)
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={self.get_slug, self.id})

class KeyWord(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_key_word")
    key_word = models.CharField(max_length=50)

    def __str__(self):
        return (self.key_word)

class BlogSubContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_sub_content")
    blog_sub_title = models.CharField(max_length=200)
    blog_sub_content = models.TextField()

    def __str__(self):
        return (self.blog_sub_title)