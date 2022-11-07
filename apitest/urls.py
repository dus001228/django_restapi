from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from apiapi.views import daejeonapiViewSet

router = routers.DefaultRouter() 
router.register('foods',daejeonapiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
