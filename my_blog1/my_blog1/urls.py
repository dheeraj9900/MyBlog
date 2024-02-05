"""
URL configuration for my_blog1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from members import views
from django.urls import path
from members.views import subscribe
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/',views.user_login,name= 'login'),
    path('signup/',views.signup,name='signup'),
    path('admin/', admin.site.urls),
    path('home/',views.members, name='members'),
    path('home/subscribe/', subscribe, name='subscribe'),
    path('home/contact/', views.contact, name='contact'),
    path('home/about/', views.about, name='about'), 
    path('details/<str:blog_id>/',views.details,name ='details'),
    path('category/<str:cat_id>/', views.category, name="category"),
    path('search/', views.search, name="search"),
    path('comments/<str:blog_id>/',views._comments,name='comments'),
    path('likes/<str:blog_id>/',views.likes,name='likes'),
    ]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)




