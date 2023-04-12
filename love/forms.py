from django import forms
from .models import Guests
from django.contrib.auth.forms import UserChangeForm as AdminForm

class GuestsSearchForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False


class UserChangeForm(AdminForm):
    class Meta:
        model = Guests
        fields = "__all__"