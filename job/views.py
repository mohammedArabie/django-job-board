from django.shortcuts import render
from .models import Job

# Create your views here.

def jobList (request):
    jobList=Job.objects.all()
    return render(request,'job/jobList.html',{"jobs":jobList})



def jobDetail(request,id):
    job=Job.objects.get(id=id)
    return render (request,'job/jobDetails.html',{'job':job})
