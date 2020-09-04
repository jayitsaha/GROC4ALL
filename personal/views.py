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
from django.shortcuts import render_to_response
from django.contrib import messages
from django.db.models import Count,Avg
from personal.models import Ratings,Reviews
import pytz
@csrf_exempt
def prediction(request):
    Text = request.POST.get('Text',False)
    TextId = request.POST.get('TextId',False)
    print(TextId)
    product = Product.objects.get(productid=TextId)

    review = Reviews.objects.create(
        text = Text,
        product = product,
        author = request.user,
        timestamp = datetime.now(pytz.timezone(settings.TIME_ZONE))
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
    context = {}
    reviews = Reviews.objects.filter(product=product).order_by('-timestamp')[:5]
    rating = Ratings.objects.filter(product=product).aggregate(Avg('rating'),Count('rating'))
    if(rating['rating__avg']==None):
        rating['rating__avg'] = 0
    else:
        rating['rating__avg'] = round(rating['rating__avg'],1)
    print(reviews)
    print(rating['rating__avg'])

    if product.quantity >= 1:
        if reviews is None :
            context = {
				'title' : product.title,
				'product': product,
				'rating': rating,
				# 'reviews':'No Feedback Available'
			}
        else:
            context = {
				'title' : product.title,
				'product': product,
				'rating': rating,
				'reviews':reviews
			}
        return render_to_response('ecom/show_load.html',context)
    else:
        messages.warning(request,'Product is not Available')
        return render_to_response('ecom/show_load.html',context)
    return redirect('pages:product_by_slug',TextId)
