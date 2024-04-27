# Definir las rutas de un aplicativo web
# from django.urls import path, include
# from api import views

#urlpatterns = [
#    path('', views.index, name="index"),
#]

# esta es la forma de crear las rutas de
# una api rest con django framework
from rest_framework import routers
from .api import ApiViewSet

ruta = routers.DefaultRouter()
ruta.register('api/empleados', ApiViewSet, 'api')

urlpatterns = ruta.urls
