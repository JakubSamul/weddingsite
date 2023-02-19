from django import forms
from .models import Guests


class GuestsSearchForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False