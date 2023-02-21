from django.urls import path, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .views import (
    GuestListView,
    HomePageView,
    LoginView,
    LogoutView,
    GiftsListView
)
from .models import Guests

urlpatterns = [
    path('', 
         HomePageView.as_view(), 
         name = 'homepage'),
    path("login/", 
         LoginView.as_view(), 
         name = "login"),
    path("logout/", 
         LogoutView.as_view(), 
         name = "logout"),
    path('guestslist/', 
         GuestListView.as_view(), 
         name = 'guests-list'),
     path('guestlist/add/', 
         CreateView.as_view(
            model = Guests,
            fields = '__all__',
            success_url = reverse_lazy('guests-list'),
            template_name = 'guests_form.html'
         ), 
         name='guestslist-add'),
     path('guestslist/<int:pk>/delete/',
          DeleteView.as_view(
               model = Guests,
               success_url = reverse_lazy('guests-list'),
               template_name = 'guests_delete.html'
          ),
          name='guestslist-delete'),
     path('guestslist/<int:pk>/edit/',
         UpdateView.as_view(
            model=Guests,
            fields='__all__',
            success_url=reverse_lazy('guests-list'),
            template_name='guests_update.html'
         ),
         name = 'guestslist-update'),
     path('giftslist/',
          GiftsListView.as_view(),
          name = 'gifts-list')
]