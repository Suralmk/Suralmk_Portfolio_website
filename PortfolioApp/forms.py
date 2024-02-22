from django import forms
from . models import Subscription

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    message = forms.Textarea()

class SubscriptionForm(forms.Form):
    class Meta:
        model = Subscription
        fields = "__all__"