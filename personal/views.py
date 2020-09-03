from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import fasttext
# Create your views here.
from personal.models import NameForm
from ecommerce.settings import model1
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from .models import Reviews, Ratings
from django.utils.timezone import datetime
from django.conf import settings

def prediction(request):
    Text = request.POST.get('Text',False)
    TextId = request.POST.get('pid',False)
    product = Product.objects.get(productid=TextId)
    
    review = Reviews.objects.create(
        text = Text,
        product = product,
        author = request.user,
    )
    review.save()
    predct = model1.predict(str(Text))
    if(predct[0][0] == '__label__1'):
        predct = 5 - (predct[1][0])*5
    else:
        predct = (predct[1][0])*5
    
    ratings = Ratings.objects.create(
        rating = predct,
        product = product,
        user = request.user,
        review = review
    )
    ratings.save()
    return redirect('pages:product_by_slug',TextId)
