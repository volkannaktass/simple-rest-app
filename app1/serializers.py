from app1.models import Kitap,Yazar
from rest_framework import serializers


class YazarSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model=Yazar
        fields=("isim","soyisim","kitaplar")

class KitapSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="app1:kitap-detail")
    class Meta:
        model=Kitap
        #"url",
        fields=("baslik",)
