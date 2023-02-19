from django.db import models
# from .forms import ChoiceSideField


class Side(models.Model):
    class Meta:
        ordering = ('name',)

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Guests(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    category = models.ForeignKey(Side, models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
