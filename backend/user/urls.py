from django.urls import path
from .views import register, logout, update_user_info
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout, name='logout'),
    path('update/', update_user_info, name='update_user_info'),
]

