from django.urls import path
from . import views

app_name = 'personal_account'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
]