from rest_framework import viewsets

from .models import Cargo
from .serializers import (CargoCreateSerializer, CargoListSerializer, CargoUpdateSerializer,
                          CargoDetailSerializer, CargoDeleteSerializer)


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CargoCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CargoUpdateSerializer
        elif self.action == 'list':
            return CargoListSerializer
        elif self.action == 'retrieve':
            return CargoDetailSerializer
        elif self.action == 'destroy':
            return CargoDeleteSerializer

