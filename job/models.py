from pickle import TRUE
from tkinter import CASCADE
from django.db import models

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
    title=models.CharField(max_length=50)
    job_type=models.CharField( max_length=50,choices=JOP_TYPE)
    discribtion=models.TextField(max_length=1500)
    published_at=models.DateTimeField(auto_now=TRUE)
                
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='jobs/')
    def __str__(self) :
        return self.title


