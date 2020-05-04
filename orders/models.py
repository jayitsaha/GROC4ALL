from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
	item = models.CharField(max_length=200)
	quantity = models.IntegerField()
	price = models.CharField(max_length=100)
	total = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	address = models.TextField()
	order_date = models.DateTimeField(default=datetime.now() , blank=True)
	user_id = models.IntegerField(blank=True)
	delivery = models.BooleanField(default=False)

	def __str__(self):
		return self.item
