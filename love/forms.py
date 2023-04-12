from django import forms
from .models import Guest
from django.contrib.auth.forms import UserChangeForm as AdminForm

class GuestSearchForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False


class UserChangeForm(AdminForm):
    class Meta:
        model = Guest
        fields = "__all__"