from django.urls import path, include
from rest_framework import routers

from .views import CargoViewSet

cargo_router = routers.SimpleRouter()
cargo_router.register('', CargoViewSet)

urlpatterns = cargo_router.urls
