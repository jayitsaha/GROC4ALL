from django.db import models
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# Create your models here.
from django import forms
import numpy as np
from ecommerce.settings import model1
from django.utils import timezone
from users.models import User
from products.models import Product
from decimal import Decimal
# nltk.download('wordnet')
# import nltk
# nltk.download('wordnet')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class Reviews(models.Model):
    text = models.CharField(max_length=1000, blank=True,null=True)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
	    return self.text


class Ratings(models.Model):
    rating = models.DecimalField(default=0.0, max_digits=2, decimal_places=1)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    review = models.ForeignKey(Reviews, on_delete = models.CASCADE,null=True)

    def __str__(self):
        return str(self.rating)
