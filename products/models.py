from django.db import models
from datetime import datetime

from categories.models import Category
# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=40,unique=True)
	price = models.CharField(max_length=200)
	quantity = models.IntegerField()
	description = models.TextField()
	photo = models.ImageField(upload_to='products/')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
	published_at = models.DateTimeField(default=datetime.now , blank=True)

	def summary(self):
		return self.description[:100] + '.....'

	def __str__(self):
		return self.title
