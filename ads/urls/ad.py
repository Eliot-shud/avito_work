from django.urls import path, include
from rest_framework import routers

from ads.views import AdViewSet

router = routers.SimpleRouter()
router.register("", AdViewSet)

urlpatterns = [
    path("", include(router.urls)),
]