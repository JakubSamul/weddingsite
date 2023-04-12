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
    AboutPageView
)
from .models import Guest, Gifts

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
    path('guestlist/', 
         GuestListView.as_view(), 
         name = 'guest-list'),
    path('guestconflist/', 
         GuestConfListView.as_view(), 
         name = 'guest-conf-list'),
    path('guestlist/add/', 
         GuestCreateView.as_view(
            model = Guest,
            fields = '__all__',
            success_url = reverse_lazy('guest-list'),
            template_name = 'guest_form.html'
         ), 
         name='guest-add'),
     path('guestlist/<int:pk>/delete/',
          DeleteView.as_view(
               model = Guest,
               success_url = reverse_lazy('guest-list'),
               template_name = 'guest_delete.html'
          ),
          name='guest-delete'),
     path('guestlist/<int:pk>/edit/',
         UpdateView.as_view(
            model=Guest,
            fields='__all__',
            success_url=reverse_lazy('guest-list'),
            template_name='guest_update.html'
         ),
         name = 'guest-update'),
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
]