from django.urls import path,include
from .views import jobDetail,jobList
app_name="job"
urlpatterns = [
    
    path('',jobList),
    path('<int:id>',jobDetail,name="job_detail")
]
