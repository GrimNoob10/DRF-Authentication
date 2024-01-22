from django.urls import path , include
from accounts.views import UserRegistration , UserLogin , UserProfile

urlpatterns = [
    path('register/' , UserRegistration.as_view() , name = 'register'),
    path('login/' , UserLogin.as_view() , name = 'login'),
    path('profile/' , UserProfile.as_view() , name = 'profile'),

]