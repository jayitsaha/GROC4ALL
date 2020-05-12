from django.db import models
from datetime import datetime


from products.models import Product
from django.contrib.auth.models import User
# Create your models here.


class WishList(models.Model):
	user_id = models.IntegerField()
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist_product')


	def __str__(self):
		return str(self.product.productid)
