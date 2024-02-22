from django.db import models


class Subscription(models.Model):
    email = models.EmailField(max_length=100)
    # country = models.CharField(max_length=50)
    # ip = models.GenericIPAddressField()


