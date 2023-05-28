from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('current_location', )


class VehicleDistanceListSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(label='Дистанция от груза до машины')

    class Meta:
        model = Vehicle
        fields = ('reg_sign', 'distance')

