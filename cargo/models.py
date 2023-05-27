from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Cargo(models.Model):
    pick_up = models.ForeignKey(
        verbose_name='Откуда груз отправлен',
        to='location.Location',
        on_delete=models.PROTECT,
        related_name='outcoming_cargos',
    )
    delivery = models.ForeignKey(
        verbose_name='Куда груз отправлен',
        to='location.Location',
        on_delete=models.PROTECT,
        related_name='incoming_cargos',
    )
    weight = models.FloatField(
        verbose_name='Масса груза',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000)
        ],
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

