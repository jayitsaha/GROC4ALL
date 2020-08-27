from django.http import HttpResponseRedirect
from django.shortcuts import render
import fasttext
# Create your views here.
from personal.models import NameForm
from ecommerce.settings import model1
from django.views.decorators.csrf import csrf_exempt
from products.models import Product

# model1 = fasttext.load_model("amazon_reviews.bin")
# pred1 = model1.predict("I hate the product")
# print("PRED1")
# print(pred1)

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/index.html')
@csrf_exempt
def prediction(request):
    #print(MODEL.summary())

    Text = request.POST.get('Text',False)
    TextId = request.POST.get('TextId',False)
    product = Product.objects.get(productid=TextId)


    print(Text)
    print(TextId)
    # Sentenceex = Sentence(str(Text))
    # predct = Sentenceex.predection()
    predct = model1.predict(str(Text))
    if(predct[0][0] == '__label__1'):
        predct = 100 - (predct[1][0])*100
    else:
        predct = (predct[1][0])*100
    #put(self, request, pk):
    print("Prediction is :",float(predct))#Sentence preparation
    ## POST request
   # model = mlmodel()
    #model.Text = Text
    #model.prediction = float(predct)
    #response = requests.post('/predictions/', data=model)

    return render(request, 'ecom/show.html', {'prediction':  round(float(predct), 2),'title' : product.title,'product': product})
