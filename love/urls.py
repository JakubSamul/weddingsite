from django.urls import path, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .views import (
    HomePageView,
    LoginView,
    LogoutView,
    ConfirmationView
)

urlpatterns = [
     path('', 
         HomePageView.as_view(), 
         name = 'homepage'),
     path('login/', 
         LoginView.as_view(), 
         name = "login"),
     path('logout/', 
         LogoutView.as_view(), 
         name = "logout"),
     path('confirmation/',
         ConfirmationView.as_view(),
         name = 'confirmation-update'),
]