from django.db.models import ExpressionWrapper, Func, F, FloatField
from django.db.models.functions import Coalesce, Radians
from .models import Vehicle


class VehicleServices:

    @staticmethod
    def get_vehicles_and_distance(cargo):
        """
        Метод аннотирует все машины дополнительным полем distance и возвращает queryset машин.
        Расчеты расстояния производятся без использования библиотеки geopy, так как при ее использовании
        возникает проблема N+1 запросов.
        :param cargo:
        :return annotated vehicles:
        """
        cargo_lat_rad = Radians(cargo.pick_up.lat)
        cargo_lng_rad = Radians(cargo.pick_up.lng)
        radius_m = 3558.8
        vehicles = Vehicle.objects.all()
        vehicles = vehicles.annotate(
            distance=Coalesce(
                ExpressionWrapper(
                    radius_m * Acos(
                        Cos(cargo_lat_rad) * Cos(Radians(F('current_location__lat'))) *
                        Cos(Radians(F('current_location__lng')) - cargo_lng_rad) +
                        Sin(cargo_lat_rad) * Sin(Radians(F('current_location__lat')))
                    ), output_field=FloatField()
                ), 0.0
            )
        )
        return vehicles


class Sin(Func):
    function = 'SIN'


class Cos(Func):
    function = 'COS'


class Acos(Func):
    function = 'ACOS'


class Radians(Func):
    function = 'RADIANS'