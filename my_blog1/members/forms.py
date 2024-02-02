# members/forms.py

from django import forms
from .models import Subscriber
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'content']
