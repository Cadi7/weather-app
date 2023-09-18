## signal, when user_weather is called from another user location, change the new location
import geocoder
from django.db.models.signals import post_save

from apps.users.models import User


def change_location(sender, instance, created, **kwargs):
    if created:
        user_location = geocoder.ip('me').city
        instance.location = user_location
        instance.save()


post_save.connect(change_location, sender=User)