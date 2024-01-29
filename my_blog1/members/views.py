

from .models import Blog,Subscriber
from .forms import SubscribeForm
from .models import Category
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User




def members(request):
  blogs = Blog.objects.order_by('-published_at')
  return render(request,"cards.html", {"blogs": blogs,'categories': Category.objects.all()})


def contact(request):
  blogs = Blog.objects.all()
  return render(request,"contact.html", {"blogs": blogs})

def details(request,blog_id):
   blog = get_object_or_404(Blog, pk=blog_id)
  #  print(blog)
   return render(request,"details.html", {"blog":blog})
  #  return render(request,"details.html", {"blogs": blogs})
  


def about(request):
  blogs = Blog.objects.all()
  return render(request,"about.html", {"blogs": blogs})




def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, 'You have already subscribed.')
            else:
                form.save()
                messages.success(request, 'Subscription successful! Thank you for subscribing.')
                
            return redirect('subscribe')
    else:
        form = SubscribeForm()

    return render(request, 'subscribe.html', {'form': form})




def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Invalid Credentials'})
        else:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('members')




def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Username already exists'})
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request,user)
                return redirect('members')  
        else:
            return render(request, 'signup.html', {'form':UserCreationForm, 'error': 'Passwords do not match'})



def logout(request):
    logout(request)
    return redirect('login')

def category(request, cat_id):
    blogs = Blog.objects.all().filter(blog_cat=cat_id)
    category_obj = Category.objects.get(id=cat_id)
    print(blogs)
    return render(request, "category.html", {"blogs": blogs, "cat_name": category_obj.name })