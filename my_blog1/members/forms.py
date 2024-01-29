# members/forms.py

from django import forms
from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'content']
