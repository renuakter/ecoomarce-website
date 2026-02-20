from django.urls import path
from . import views



urlpatterns = [
    path('', views.registerpage, name='registerpage'),
    path('login/', views.loginpage, name='loginpage'),
    path('homepage', views.homepage, name='homepage'),
    path("logout/", views.logoutpage, name="logoutpage"),
]
