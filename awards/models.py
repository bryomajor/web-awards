from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from url_or_relative_url_field.fields import URLOrRelativeURLField
from django.core.validators import MaxValueValidator

# Create your models here.
class Profile(models.Model):
    bio = HTMLField()
    profile_photo = ImageField(blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=12)

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


class Projects(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    image_landing = models.ImageField(upload_to = 'landing/')
    description = HTMLField(max_length=200, blank=True)
    link = URLOrRelativeURLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_projects_by_profile(cls, profile):
        projects = Projects.objects.filter(profile__pk=profile)
        return projects

    


    def __str__(self):
        return self.title


class Rates(models.Model):
    design = models.IntegerField(default=0, validators=[MaxValueValidator(10)])
    usability = models.IntegerField(default=0, validators=[MaxValueValidator(10)])
    content = models.IntegerField(default=0, validators=[10])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.IntegerField(default=0)

    class Meta:
        unique_together = (('user', 'design', 'usability', 'content', 'project'))
        index_together = (('user', 'design', 'usability', 'content', 'project'))

        ordering = ['-id']
    
    def save_rate(self):
        self.save()

    def _get_total(self):
        return (self.design + self.usability + self.content) * 0.33

    total = property(_get_total)

    @classmethod
    def get_rates(cls, id):
        rates = cls.objects.all()
        return rates
       

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField(max_length=400)
    pro_id = models.IntegerField(default=0)