from django.db import models


class Subscription(models.Model):
    email = models.EmailField(max_length=100)


    def __str__(self):
        return  str(self.email)


