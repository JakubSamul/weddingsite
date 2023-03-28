from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
# from .forms import ChoiceSideField


class Guests(models.Model):
    FOODS = [
        ('WEGE','wegeterianskie'),
        ('MEAT','miesne')
    ]
    SIDE = [
        ('KUBA','Kuba'),
        ('BASIA','Basia')
    ]
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    side = models.CharField(choices=SIDE, null=True, blank=True, max_length=5)
    confirmation = models.BooleanField(default=False, blank=True)
    accompanying = models.ManyToManyField('Guests', null=True, blank=True)
    preferences = models.CharField(choices=FOODS, null=True, blank=True, max_length=4)

    def __str__(self):
        return f'{self.name}'
    

class Gifts(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
@receiver(m2m_changed, sender=Guests.accompanying.through)
def update_persons(sender, instance, **kwargs):
    for person in instance.accompanying.all():
        if kwargs.get("action") == "post_add":
            if instance not in person.accompanying.all():
                person.accompanying.add(instance)
                person.save()
            