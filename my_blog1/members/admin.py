from django.contrib import admin
from .models import Blog,Subscriber,Category,Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Subscriber)
admin.site.register(Category)
admin.site.register(Comment)



