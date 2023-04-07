from django.urls import path, include
from rest_framework import routers
from . import views

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register('exchanges', ExchangeViewSet)
router.register('securities', SecurityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
