from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

'''
create a profile if a user has been created
runs every time an object is saved to database
incl. when an account is created and saved
'''
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
