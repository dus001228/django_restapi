from telnetlib import STATUS
from rest_framework import viewsets
from .serializers import *
from .models import *

class daejeonapiViewSet(viewsets.ModelViewSet):
    queryset = daejeonfood.objects.all()
    serializer_class = daejeonapiSerializer

class daejeonnewsViewSet(viewsets.ModelViewSet):
    queryset = daejeonnews.objects.all()
    serializer_class = daejeonnewsSerializer

class daejeonweatherViewSet(viewsets.ModelViewSet):
    queryset = daejeonweather.objects.all()
    serializer_class = daejeonweatherSerializer

class daejeontourViewSet(viewsets.ModelViewSet):
    queryset = daejeontour.objects.all()
    serializer_class = daejeontourSerializer

class daejeonrestViewSet(viewsets.ModelViewSet):
    queryset = daejeonrest.objects.all()
    serializer_class = daejeonrestSerializer
