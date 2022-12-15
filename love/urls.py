from django.urls import path
from .views import (
    GuestView,
    GuestListView,
    HomePageView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('guest/', GuestView.as_view(), name='guest'),
    path('guestslist/', GuestListView.as_view(), name='guests-list')
]