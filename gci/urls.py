from django.conf.urls import url, include
from .models import *
from .serializers import *
from .views import *
from rest_framework import serializers, viewsets, routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)
router.register(r'group', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]