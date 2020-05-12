from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from products.models import Product
class Order(models.Model):
	item = models.CharField(max_length=200)
	productid = models.ForeignKey(Product , on_delete = models.CASCADE)
	quantity = models.IntegerField()
	price = models.CharField(max_length=100)
	total = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	address = models.TextField()
	order_date = models.DateTimeField(default=timezone.now() , blank=True)
	user_id = models.IntegerField(blank=True)
	delivery = models.BooleanField(default=False)

	def __str__(self):
		return self.item
