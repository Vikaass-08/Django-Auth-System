from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,models.CASCADE)    #to save all the previous data on User in user such as name,surname,email,etc.
    

    #additional information
    portfolio_site= models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username
