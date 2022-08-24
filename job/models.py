from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

JOP_TYPE=(
    ('FULL TIME','FULL TIME'),
    ('PART TIME','PART TIME')
)



class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
    

class Job (models.Model):
    owner=models.ForeignKey(User, related_name=("job_owener"), on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    job_type=models.CharField( max_length=50,choices=JOP_TYPE)
    discribtion=models.TextField(max_length=1500)
    published_at=models.DateTimeField(auto_now=TRUE)
                
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='jobs/')
    slug=models.SlugField(null=True,blank=True)
    def save(self,*args,**kwargs ):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)
    def __str__(self) :
        return self.title

class Apply (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    cv=models.FileField(upload_to='apply/')
    web_site=models.URLField()
    cover_letter =models.TextField(max_length=500)
    job=models.ForeignKey(Job, related_name=("apply_job"), on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=TRUE)

    def __str__ (self):
        return self.name
