from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True,verbose_name='Date Of Birth')
    SEX=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    gender=models.CharField(choices=SEX,max_length=10,default="----")
    mobile=models.IntegerField(verbose_name='Mobile No.',blank=True,default=None,null=True)
    aadhar_no=models.IntegerField(verbose_name='Aadhar No.',blank=True,default=None,null=True)
    acertificate=models.FileField(upload_to='aadhar',verbose_name='Upload Aadhar Card ',default=None,null=True)
    address=models.CharField(max_length=500,verbose_name='Address',blank=True,default=None,null=True)
    bcertificate=models.FileField(upload_to='blind',verbose_name='Upload Blind Identity Certificate',default=None,null=True)
    experience=models.IntegerField(verbose_name='Work Experience',default=None,null=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
