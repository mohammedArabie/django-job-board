from django.urls import path,include
from .views import add_job, jobDetail,jobList
app_name="job"
urlpatterns = [
    
    path('',jobList , name="job_list"),
    path('add',add_job,name="add_job"),
    path('<str:slug>',jobDetail,name="job_detail")
]
