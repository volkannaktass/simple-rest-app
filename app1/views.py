from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app1.models import Yazar,Kitap
from app1.serializers import YazarSerializer,KitapSerializer

from app1.utils.constants import PostStatus
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class YazarViewSet(viewsets.ModelViewSet):

    queryset = Yazar.objects.all()
    serializer_class = YazarSerializer


class KitapViewSet(viewsets.ModelViewSet):

    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer



@method_decorator(name='get', decorator=swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            'detail_slug', openapi.IN_QUERY,
            description=("A unique string value identifying requested post"),
            type=openapi.TYPE_STRING,
            enum=[ps.value for ps in PostStatus],
            required=True
        ),
    ]
))
class PingView(APIView):

    def get(self, *args, **kwargs):
        return Response({'ping': 'pong'}, status=status.HTTP_200_OK)
