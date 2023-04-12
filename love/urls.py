from django.urls import path, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .views import (
    GuestListView,
    HomePageView,
    LoginView,
    LogoutView,
    GiftsListView,
    GuestCreateView,
    GuestConfListView,
    ServicesPageView,
    AboutPageView,
    ConfirmationView
)
from .models import Guests, Gifts

urlpatterns = [
    path('', 
         HomePageView.as_view(), 
         name = 'homepage'),
     path('', 
         AboutPageView.as_view(), 
         name = 'about'),
    path('', 
         ServicesPageView.as_view(), 
         name = 'services'),
    path('login/', 
         LoginView.as_view(), 
         name = "login"),
    path('logout/', 
         LogoutView.as_view(), 
         name = "logout"),
    path('guestslist/', 
         GuestListView.as_view(), 
         name = 'guests-list'),
    path('guestsconflist/', 
         GuestConfListView.as_view(), 
         name = 'guests-conf-list'),
    path('guestslist/add/', 
         GuestCreateView.as_view(
            model = Guests,
            fields = '__all__',
            success_url = reverse_lazy('guests-list'),
            template_name = 'guests_form.html'
         ), 
         name='guests-add'),
     path('guestslist/<int:pk>/delete/',
          DeleteView.as_view(
               model = Guests,
               success_url = reverse_lazy('guests-list'),
               template_name = 'guests_delete.html'
          ),
          name='guests-delete'),
     path('guestslist/<int:pk>/edit/',
         UpdateView.as_view(
            model=Guests,
            fields='__all__',
            success_url=reverse_lazy('guests-list'),
            template_name='guests_update.html'
         ),
         name = 'guests-update'),
     path('giftslist/',
          GiftsListView.as_view(),
          name = 'gifts-list'),
     path('giftslist/add/', 
         CreateView.as_view(
            model = Gifts,
            fields = '__all__',
            success_url = reverse_lazy('gifts-list'),
            template_name = 'gifts_form.html'
         ), 
         name='gifts-add'),
     path('giftslist/<int:pk>/delete/',
          DeleteView.as_view(
               model = Gifts,
               success_url = reverse_lazy('gifts-list'),
               template_name = 'gifts_delete.html'
          ),
          name='gifts-delete'),
     path('giftslist/<int:pk>/edit/',
         UpdateView.as_view(
            model=Gifts,
            fields='__all__',
            success_url=reverse_lazy('gifts-list'),
            template_name='gifts_update.html'
         ),
         name = 'gifts-update'),
     path('confirmation/',
         ConfirmationView.as_view(
          success_url=reverse_lazy('homepage')
         ),
         name = 'confirmation-update'),
]