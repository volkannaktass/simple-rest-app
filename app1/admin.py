from django.contrib import admin

# Register your models here.
from app1.models import Kitap,Yazar

admin.site.register(Kitap)
admin.site.register(Yazar)
