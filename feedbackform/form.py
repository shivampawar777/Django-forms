from django import forms
from .models import Formdata

class FeedbackForm(forms.Form):
    name=forms.CharField(label="Full Name", max_length=100)
    email=forms.EmailField(label="Email", max_length=100)
    phone=forms.CharField(label="Contact No.", max_length=100)
    rating=forms.IntegerField(label="Rate our service from 1 to 5")
    feedback=forms.CharField(label="Please provide your feedback", widget=forms.Textarea)





