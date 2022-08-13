from django.urls import path,include
from .views import jobDetail,jobList
urlpatterns = [
    
    path('',jobList),
    path('<int:id>',jobDetail)
]
