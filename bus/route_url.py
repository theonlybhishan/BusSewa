from django.db import router
from . import route_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'getproperty', route_views.ServiceApi,basename = "getproperty"),