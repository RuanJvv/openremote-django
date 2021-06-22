import json
from django.http.response import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get data from request
            data = request.GET.get('data')
            # vectorize data
            vector = PredictorConfig.vectorizer.transform([data])
            # predict based on vector
            prediction = PredictorConfig.regressor.predict(vector)[0]
            # build response
            response = {prediction}
            # return response
            return JsonResponse(response)
