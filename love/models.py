from django.db import models
# from .forms import ChoiceSideField


class Guests(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    CHOICE_SIDE = [('K', 'Jakub'), ('B', 'Barbara')]
    choice = ''
    side = models.CharField(max_length=2, choices=CHOICE_SIDE, default=choice)

    def __str__(self):
        return self.name
