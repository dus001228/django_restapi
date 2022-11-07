from telnetlib import STATUS
from rest_framework import viewsets
from .serializers import daejeonapiSerializer
from .models import daejeonfood

class daejeonapiViewSet(viewsets.ModelViewSet):
    queryset = daejeonfood.objects.all()
    serializer_class = daejeonapiSerializer