
# from .models import Blog,Subscriber

# from .forms import SubscribeForm
# from .models import Category
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
# from django.db.models import Q
# from django.core.paginator import Paginator
# from .forms import CommentForm


from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import SubscribeForm, CommentForm
from .models import Blog, Subscriber, Category,Comment


def members(request):
  blogs = Blog.objects.order_by('-published_at')
  categories = Category.objects.all()
  
  pageNumber = request.GET.get("page")
  
  if pageNumber is None:
    pageNumber = 2

  paginatedBlogs = Paginator(blogs, 2)
  pagedBlogs = paginatedBlogs.page(pageNumber)
  
  return render(request,"cards.html", {'blogs': pagedBlogs,'categories': categories})

def search(request):
    if request.method == "POST":
        x =request.POST.get('prod_search')
        print(x)
        mydata = Blog.objects.filter(Q(cardTitle__icontains = x)| Q(cardDescription__icontains = x))
        print(mydata)
        # return redirect('members')
        return render(request,"cards.html", {"blogs": mydata})


    


def contact(request):
  blogs = Blog.objects.all()
  return render(request,"contact.html", {"blogs": blogs})

def details(request,blog_id):
   blog = get_object_or_404(Blog, pk=blog_id)
#    print(blog)
   if blog:
       #updating view count
       blog.views += 1
       blog.save()
       
   comments_list = Comment.objects.filter(blog_id=blog_id)
   return render(request,"details.html", {"blog":blog,"comments_list":comments_list})


def likes(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    print(blog)
    if blog:
        blog.likesCount+=1
        blog.save()
    return redirect('/details/'+blog_id+'/')
  
#  def comment(request,blog_id):
     
    


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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form':form, 'error': form.errors})



def logout(request):
    logout(request)
    return redirect('login')

def category(request, cat_id):
    blogs = Blog.objects.all().filter(blog_cat=cat_id)
    category_obj = Category.objects.get(id=cat_id)
    print(blogs)
    return render(request, "category.html", {"blogs": blogs, "cat_name": category_obj.name })



def _comments(request,blog_id):
        com = request.POST.get('comment1')
        print(com)
        x = Comment(body=com, blog_id=blog_id)
        x.save()
        return redirect('/details/'+blog_id+"/")





