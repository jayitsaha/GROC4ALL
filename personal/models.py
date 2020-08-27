from django.db import models
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# Create your models here.
from django import forms
import numpy as np
from ecommerce.settings import model1
# nltk.download('wordnet')
# import nltk
# nltk.download('wordnet')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


