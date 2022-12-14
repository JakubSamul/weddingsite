from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import GuestViev, GuestListView

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # the'name' values as called by the {% url %} template tag
    path('guest/', GuestViev.as_view(), name='guest'),
    path('guestslist', GuestListView.as_view(), name='guests-list')
]