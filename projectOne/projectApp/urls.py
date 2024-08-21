from django.contrib import admin
from django.urls import path
from projectApp import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('',views.signup,name='signup'),
]
