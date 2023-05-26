import re
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Vehicle(models.Model):
    reg_sign = models.CharField(
        verbose_name='Регистрационный номер',
        unique=True,
        max_length=5,
    )
    current_location = models.ForeignKey(
        verbose_name='Текущая локация',
        to='location.Location',
        on_delete=models.PROTECT,
        related_name='inner_vehicles',
    )
    load_capacity = models.FloatField(
        verbose_name='Грузоподъемность',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000),
        ],
    )

    def clean(self):
        if re.match(r'^[1-9]\d{3}[A-Z]$', str(self.reg_sign)) is None:
            raise ValidationError('Некорректный регистрационный номер')
