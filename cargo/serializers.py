from rest_framework import serializers

from location.serializers import LocationDetailSerializer
from vehicle.serializers import VehicleDistanceListSerializer
from vehicle.services import VehicleServices
from .models import Cargo


class CargoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = ('pick_up', 'delivery', 'weight', 'description')


class CargoListSerializer(serializers.ModelSerializer):
    vehicles_closer_450_count = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('pick_up', 'delivery', 'vehicles_closer_450_count')

    def get_vehicles_closer_450_count(self, cargo):
        vehicles_closer_450_count = len(VehicleServices.get_vehicles_and_distance(cargo).filter(distance__lte=450))
        return vehicles_closer_450_count


class CargoDetailSerializer(serializers.ModelSerializer):
    pick_up = LocationDetailSerializer()
    delivery = LocationDetailSerializer()
    vehicles = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('pick_up', 'delivery', 'weight', 'description', 'vehicles')

    def get_vehicles(self, cargo):
        vehicles_and_distance = VehicleServices.get_vehicles_and_distance(cargo)
        return VehicleDistanceListSerializer(vehicles_and_distance, many=True).data


class CargoUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = ('weight', 'description')


class CargoDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = ('pk', )
