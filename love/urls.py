from django.urls import path
from django.views.generic import CreateView, UpdateView, DeleteView
from .views import (
    GuestListView,
    HomePageView,
    LoginView,
    LogoutView
)
from .models import Guests

urlpatterns = [
    path('', 
         HomePageView.as_view(), 
         name='homepage'),
    path("login/", 
         LoginView.as_view(), 
         name="login"),
    path("logout/", 
         LogoutView.as_view(), 
         name="logout"),
    path('guest/', 
         CreateView.as_view(
            model=Guests,
            fields='__all__',
            template_name='guests_form.html'
         ), 
         name='guest'),
    path('guestslist/', 
         GuestListView.as_view(), 
         name='guests-list')
]