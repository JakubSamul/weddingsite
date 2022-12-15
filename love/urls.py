from django.urls import path
from .views import GuestView, GuestListView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('guest/', GuestView.as_view(), name='guest'),
    path('guestslist/', GuestListView.as_view(), name='guests-list')
]