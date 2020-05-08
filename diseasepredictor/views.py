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

        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])

        user_data = np.array(
            (age,
             sex,
             cp,
             trestbps,
             chol
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
            value = 'may have covid-19, do get checked'
        elif int(predictions[0]) == 0:
            value = "don\'t have covid-19"

    return render(request,
                  'diseasepredictor/covid1.html',
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

        radius = float(request.POST['radius'])
        texture = float(request.POST['texture'])
        perimeter = float(request.POST['perimeter'])
        area = float(request.POST['area'])
        smoothness = float(request.POST['smoothness'])

        rf = RandomForestClassifier(
            n_estimators=16, criterion='entropy', max_depth=5)
        rf.fit(np.nan_to_num(X), Y)

        user_data = np.array(
            (radius,
             texture,
             perimeter,
             area,
             smoothness)
        ).reshape(1, 5)

        predictions = rf.predict(user_data)
        print(predictions)

        if int(predictions[0]) == 1:
            value = 'may have covid-19, do get tested'
        elif int(predictions[0]) == 0:
            value = "don\'t have covid-19"

    return render(request,
                  'diseasepredictor/covid2.html',
                  {
                      'context': value
                  })


def home(request):

    return render(request,
                  'diseasepredictor/home.html')

# def handler404(request):
#     return render(request, '404.html', status=404)
