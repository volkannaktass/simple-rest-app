
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app1 import views



from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


#router = routers.DefaultRouter()
#router.register(r'yazarlar', views.YazarViewSet)
#router.register(r'kitaplar', views.KitapViewSet)



schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)
#^{prefix}/{pk}/get_detail/$

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    #path('myapi/',include(router.urls))
   path('api/v1/', 
        include([
            #name="app1"
            path('app1/', include('app1.urls')),
            path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
        ])
    ),
]
