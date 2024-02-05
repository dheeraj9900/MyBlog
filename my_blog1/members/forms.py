# members/forms.py

from django import forms
from .models import Subscriber
from .models import Comment
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','body']
