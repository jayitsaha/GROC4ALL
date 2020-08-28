from django.db import models
# from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    location = models.CharField(max_length=200,default='')
    office_name = models.CharField(max_length=200,default='')


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profile/',default='default.jpg')

	def __str__(self):
		return self.user.username

	def save(self,*args,**kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)

		if img.height  > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Seller(models.Model):
	user = models.OneToOneField(User , on_delete=models.CASCADE ,primary_key=True )

	def __str__(self):
		return self.user.username