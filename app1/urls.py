
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app1 import views




router = routers.DefaultRouter()
router.register(r'yazarlar', views.YazarViewSet)
router.register(r'kitaplar', views.KitapViewSet)


#app_name = "app1"
urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    #path('ping/',views.PingView.as_view(),include(router.urls),name='ping')
    path('ping/', views.PingView.as_view(), name='ping'),
] + router.get_urls()

