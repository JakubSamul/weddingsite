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


class UserChangeForm2(AdminForm):
    others = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], required=False)
    class Meta:
        model = Guests
        fields = ["confirmation", "others", "preferences"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['others'].choices = [(l.id, f"{l.name} {l.surname}") for l in self.instance.accompanying.all()]
        self.fields['others'].initial = [l.id for l in self.instance.accompanying.filter(confirmation=True)]

    def save(self, commit=True):
        obj = super().save(commit=commit)
        for person in obj.accompanying.all():
            if str(person.id) in self.cleaned_data["others"]:
                person.confirmation = True
                person.save()
            else:
                person.confirmation = False
                person.save()
        return obj