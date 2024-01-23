from django.urls import path , include
from accounts.views import ( UserPasswordReset ,
     UserRegistration , UserLogin , UserProfile , UserChangePassword , SendPasswordResetEmail)

urlpatterns = [
    path('register/' , UserRegistration.as_view() , name = 'register'),
    path('login/' , UserLogin.as_view() , name = 'login'),
    path('profile/' , UserProfile.as_view() , name = 'profile'),
    path('changepass/' , UserChangePassword.as_view() , name = 'changepassword'),
    path('resetpassword/' , SendPasswordResetEmail.as_view() , name = 'resetpasswordemail'),
    path('resetpassword/<uid>/<token>/' , UserPasswordReset.as_view() , name = 'resetpassword'),

]