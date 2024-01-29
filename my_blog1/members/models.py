
from django.db import models
from ckeditor .fields import RichTextField

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Category(models.Model):
   name = models.CharField(max_length = 200,unique = True)
   def __str__(self):
      return self.name
   

class Blog(models.Model):
  id  = models.AutoField(primary_key=True)
  cardTitle = models.CharField(max_length=50)
  cardDescription = models.CharField(max_length=200)
  lastUpdated = models.DateTimeField(auto_now_add=True)
  cardImage = models.ImageField(upload_to='images')
  content = RichTextField(blank=True)
  blog_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
  published_at = models.DateTimeField(auto_now_add=True, null=True)



  def __str__(self):
    return self.cardTitle
  

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email




# class BlogPost(models.Model):
#     title = models.CharField(max_length=100)
#     content = RichTextField(blank=True)
   
   