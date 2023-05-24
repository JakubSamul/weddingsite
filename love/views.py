from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView
)
from .models import Guests
from .forms import GuestsSearchForm, UserChangeForm2
from .reports import summary_per_category
from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserCheck(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class GuestListView(SuperUserCheck, ListView):
    model = Guests
    template_name = 'guests_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = GuestsSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)
           
        return super().get_context_data(
            form=form,
            object_list=queryset,
            **kwargs)


class GuestConfListView(ListView):
    model = Guests
    template_name = 'guestsconf_list.html'


class HomePageView(TemplateView):
    template_name = 'index.html'


class LoginView(LoginView):
    template_name = "login.html"
    success_url = "index.html"


class LogoutView(LogoutView):
    template_name = "logout.html"


class ConfirmationView(UpdateView):
    model = Guests
    form_class = UserChangeForm2
    success_url = reverse_lazy('homepage')
    template_name = "confirmation.html"

    def get_object(self):
        return get_object_or_404(Guests, id=self.request.user.id)
    
class PreferencesView(UpdateView):
    model = Guests
    form_class = UserChangeForm2
    success_url = reverse_lazy('homepage')
    template_name = "preferences.html"

    def get_object(self):
        return get_object_or_404(Guests, id=self.request.user.id)
    
class BusView(UpdateView):
    model = Guests
    fields = ["bus_from_k", "bus_from_b", "choice_bus"]
    success_url = reverse_lazy('homepage')
    template_name = "bus.html"

    def get_object(self):
        return get_object_or_404(Guests, id=self.request.user.id)

