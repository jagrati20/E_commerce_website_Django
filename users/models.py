from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sum=models.DecimalField(max_digits=10000,decimal_places=2,blank=True,null=True)

    def __self__(self):
        return f'{self.user.username} Cart'



