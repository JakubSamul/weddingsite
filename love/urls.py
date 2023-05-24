from django.urls import path, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .views import (
    HomePageView,
    LoginView,
    LogoutView,
    ConfirmationView,
    PreferencesView,
    BusView
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
    path('preferences/',
         PreferencesView.as_view(),
         name = 'preferences-update'),
    path('bus/',
         BusView.as_view(),
         name = 'bus-update'),
]