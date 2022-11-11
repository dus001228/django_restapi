from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from apiapi.views import *

router = routers.DefaultRouter() 
router.register('foods',daejeonapiViewSet)
router.register('news',daejeonnewsViewSet)
router.register('weather',daejeonweatherViewSet)
router.register('tour',daejeontourViewSet)
router.register('rest',daejeonrestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
