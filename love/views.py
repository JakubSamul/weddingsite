from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView
)
from .models import Guests


@method_decorator(login_required, name="dispatch")
class GuestView(CreateView):
    model = Guests
    fields = ['name', 'surname']
    success_url = '/guestslist'


@method_decorator(login_required, name="dispatch")
class GuestListView(ListView):
    model = Guests
    template_name = 'guests_list.html'


class HomePageView(TemplateView):
    template_name = 'homepage.html'
