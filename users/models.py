from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension
from PIL import Image
from django.dispatch import receiver 
from django.db.models.signals import post_save


class Contact(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)
    subject=models.CharField(max_length=100,null=False,blank=False)
    message=models.TextField(null=False,blank=False)
    contacted_by=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    contacted_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

gender_choices = {
    ("Male","Male"),
    ("Female","Female"),
}


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpeg',upload_to='Profile_Pics',blank=True,null=False,validators=[validate_image_file_extension])
    about=models.TextField(blank=True,default='About Section')
    phone_no=models.CharField(max_length=10,blank=True,null=True)
    gender = models.CharField(max_length=20, choices=gender_choices,blank=True)
    
    def __str__(self):
        return  str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.height <300 or img.width > 300 or img.width <300:
            output_size = (282, 282)
            img.thumbnail(output_size)
            img.save(self.image.path)