from rest_framework import serializers
from .models import daejeonfood

class daejeonapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = daejeonfood # 모델 설정
        fields = ('id', 'title', 'new_add', '소재지주소', '지정일자', '음식의유형', '주된음식종류', 'call', 'img_url')
