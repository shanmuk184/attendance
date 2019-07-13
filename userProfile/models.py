from django.db import models

# Create your models here.
from appAuth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import TimeStampedModel

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group,related_name='groups' , blank=True)
    birth_date = models.DateField(null=True, blank=True)
    class Meta:
        permissions = [('is_admin', 'is admin'),
                       ('is_employee', 'is employee'),
                       ('can_view_attendance_lists', 'can view attendance lists')]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
