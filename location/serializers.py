from rest_framework import serializers
from .models import Location


class LocationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
