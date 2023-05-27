from rest_framework import routers

from .views import VehicleViewSet

vehicle_router = routers.SimpleRouter()
vehicle_router.register('', VehicleViewSet)

urlpatterns = vehicle_router.urls
