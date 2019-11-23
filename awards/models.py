from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    bio = HTMLField()
    photo = ImageField(blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    @receiver(post_save, sender = User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile


    def __str__(self):
        return self.bio