from django.urls import path,include
from .views import  profile_edit, signup,profile
app_name="accounts"
urlpatterns = [
    
    path('signup',signup , name="signup"),
    path('profile',profile , name="profile"),
    path('profile/',profile , name="profile"),
    path('profile/edit',profile_edit , name="profile_edit"),
    
]
