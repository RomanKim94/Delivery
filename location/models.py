from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Location(models.Model):
    city = models.CharField(
        verbose_name='Город',
        max_length=100,
    )
    state = models.CharField(
        verbose_name='Штат',
        max_length=100,
    )
    zip = models.CharField(
        verbose_name='Почтовый индекс',
        max_length=15,
    )
    lat = models.FloatField(
        verbose_name='Широта',
        validators=[
            MinValueValidator(-90),
            MaxValueValidator(90)
        ],
    )
    lng = models.FloatField(
        verbose_name='Долгота',
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180)
        ],
    )
