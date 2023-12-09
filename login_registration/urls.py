from django.contrib import admin
from django.urls import path
from login_registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logoutpage, name='logout'),
]