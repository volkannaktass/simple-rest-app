
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app1 import views

router = routers.DefaultRouter()
router.register(r'yazarlar', views.YazarViewSet)
router.register(r'kitaplar', views.KitapViewSet)

#^{prefix}/{pk}/get_detail/$

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('myapi/',include(router.urls))
]
