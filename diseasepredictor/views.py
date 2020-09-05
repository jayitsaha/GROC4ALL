from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


def covid1(request):
    df = pd.read_csv('static/covid11.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]
    value = ''

    if request.method == 'POST':

        temp = request.POST['temp']
        age = request.POST['age']
        bp = request.POST['bp']
        nose = request.POST['nose']
        breath = request.POST['breath']

        if bp=='Yes' or bp == 'yes' or bp=='YES':
            bp=1
        elif bp=='No' or bp == 'no' or bp=='NO':
            bp=0
        
        else:
            return render(request,
                  'diseasepredictor/rforest.html',
                  {
                      'context': value,
                      'error':"Please enter correct data"
                })
        
        if nose=='Yes' or nose == 'yes' or nose=='YES':
            nose=1
        elif nose=='No' or nose == 'no' or nose=='NO':
            nose=0
        else:
            return render(request,
                  'diseasepredictor/rforest.html',
                  {
                      'context': value,
                      'error':"Please enter correct data"
                })
        if breath=='Yes' or breath == 'yes' or breath=='YES':
            breath=1
        elif breath=='No' or breath == 'no' or breath=='NO':
            breath=0
        else:
            return render(request,
                  'diseasepredictor/rforest.html',
                  {
                      'context': value,
                      'error':"Please enter correct data"
                })

        user_data = np.array(
            (temp,
             bp,
             age,
             nose,
             breath
            )
        ).reshape(1, 5)

        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)

        if int(predictions[0]) == 1:
            value = 'You May have COVID-19 Virus. Kindly get in contact with a Doctor!!!'
        elif int(predictions[0]) == 0:
            value = "You are SAFE!!!"

    return render(request,
                  'diseasepredictor/rforest.html',
                  {
                      'context': value
                  })
def covid2(request):
    df = pd.read_csv('static/covid22.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1]
    print(X.shape, Y.shape)

    value = ''
    if request.method == 'POST':

        temp = request.POST['temp']
        age = request.POST['age']
        bp = request.POST['bp']
        nose = request.POST['nose']
        breath = request.POST['breath']

        if bp=='Yes' or bp == 'yes' or bp=='YES':
            bp=1
        elif bp=='No' or bp == 'no' or bp=='NO':
            bp=0
        
        else:
            return render(request,
                  'diseasepredictor/rforest.html',
                  {
                      'context': value,
                      'error':"Please enter correct data"
                })
        
        if nose=='Yes' or nose == 'yes' or nose=='YES':
            nose=1
        elif nose=='No' or nose == 'no' or nose=='NO':
            nose=0
        else:
            return render(request,
                  'diseasepredictor/knn.html',
                  {
                      'context': value,
                      'error':"Please enter correct data"
                })
        if breath=='Yes' or breath == 'yes' or breath=='YES':
            breath=1
        elif breath=='No' or breath == 'no' or breath=='NO':
            breath=0
        else:
            return render(request,
                  'diseasepredictor/knn.html',
                  {
                      'context': value,
                      'error':"Please enter correct data"
                })

        user_data = np.array(
            (temp,
             bp,
             age,
             nose,
             breath
            )
        ).reshape(1, 5)


        rf = KNeighborsClassifier()
        rf.fit(np.nan_to_num(X), Y)

        predictions = rf.predict(user_data)
        print(predictions)

        if int(predictions[0]) == 1:
            value = 'You May have COVID-19 Virus. Kindly get in contact with a Doctor!!!'
        elif int(predictions[0]) == 0:
            value = "You are SAFE!!!"

    return render(request,
                  'diseasepredictor/knn.html',
                  {
                      'context': value
                  })


def home(request):

    return render(request,
                  'diseasepredictor/predict.html')

# def handler404(request):
#     return render(request, '404.html', status=404)
