from django.urls import path , include
from accounts.views import UserRegistration

urlpatterns = [
    path('register/' , UserRegistration.as_view() , name = 'register')

]