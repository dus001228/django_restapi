from rest_framework import serializers
from .models import *

class daejeonapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = daejeonfood # 모델 설정
        fields = ('__all__')


class daejeonnewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = daejeonnews # 모델 설정
        fields = ('__all__')

class daejeonweatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = daejeonweather # 모델 설정
        fields = ('__all__')

class daejeontourSerializer(serializers.ModelSerializer):
    class Meta:
        model = daejeontour # 모델 설정
        fields = ('__all__')

class daejeonrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = daejeonrest # 모델 설정
        fields = ('__all__')
