from django.shortcuts import render,redirect,reverse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
from django.urls import reverse

# Create your views here.

def jobList (request):
    jobList=Job.objects.all()
    paginator = Paginator(jobList,1) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'job/jobList.html',{"jobs":page_obj})



def jobDetail(request,slug):
    job=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.job=job
            myform.save()
    else :
        form=ApplyForm()
    return render (request,'job/jobDetails.html',{'job':job ,'form':form})

def add_job (request):
    if request.method=='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid :
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect (reverse('jobs:job_list'))

    else:
        form=JobForm()
    
    return render(request,'job/addJob.html',{'form':form})