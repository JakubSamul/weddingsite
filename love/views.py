from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView
)
from .models import Guests, Gifts, Side
from .forms import GuestsSearchForm
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


class GiftsListView(ListView):
    model = Gifts
    template_name = 'gifts_list.html'


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class LoginView(LoginView):
    template_name = "login.html"


class LogoutView(LogoutView):
    template_name = "logout.html"


class SideCreateView(SuperUserCheck, CreateView):
    model = Side
    template_name = 'side_form.html'


class GuestCreateView(SuperUserCheck, CreateView):
    model = Guests
    template_name = 'side_form.html'

