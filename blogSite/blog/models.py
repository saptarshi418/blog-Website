from django.db import models
from django.contrib.auth.models import  User
from tinymce.models import HTMLField
from django.utils.text import slugify
# Create your models here.


#catagories
class Categories(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


#create blog

class WriteBlog(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    categories = models.ForeignKey(Categories , on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    
    coverImg = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = HTMLField()

    

    def __str__(self):
        return f'{self.user.username} - {self.title}'
    