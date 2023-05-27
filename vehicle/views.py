from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleUpdateSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return VehicleUpdateSerializer
        return super().get_serializer_class()
