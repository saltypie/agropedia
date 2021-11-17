from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from django.views.decorators.clickjacking import xframe_options_exempt


import pandas as pd                                                       
from sklearn import preprocessing                              
from sklearn.neighbors import KNeighborsClassifier                       
import numpy as np   
from . import suggest



# Create your views here.
                 
class PlantsSuggest(APIView):
    def get(self, request, *args,**kwargs):
        query = self.kwargs.get('params', None)
        query = query.replace("%20", " ")
        res = suggest.suggester(query)
        return Response({'songs':res})            