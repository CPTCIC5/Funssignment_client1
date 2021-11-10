from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)
    subject=models.CharField(max_length=100,null=False,blank=False)
    message=models.TextField(null=False,blank=False)
    contacted_by=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    contacted_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name