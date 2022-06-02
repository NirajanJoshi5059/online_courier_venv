from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Gender(models.Model):
    gender_type=models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.gender_type)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.gender_type='male'


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50, blank=True, null=True)
    middle_name=models.CharField(max_length=50, blank=True, null=True)
    last_name=models.CharField(max_length=50, blank=True, null=True)
    profile_avatar=models.ImageField(upload_to='user_profile/', null=True, blank=True)
    address=models.CharField(max_length=50, blank=True, null=True)
    contact=models.CharField(max_length=20, blank=True, null=True)
    bank_account_no=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)