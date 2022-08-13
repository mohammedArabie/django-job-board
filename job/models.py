from pickle import TRUE
from django.db import models

# Create your models here.

JOP_TYPE=(
    ('FULL TIME','FULL TIME'),
    ('PART TIME','PART TIME')
)

class Job (models.Model):
    title=models.CharField(max_length=50)
    jopType=models.CharField( max_length=50,choices=JOP_TYPE)
    discribtion=models.TextField(max_length=1500)
    published_at=models.DateTimeField(auto_now=TRUE)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    def __str__(self) :
        return self.title