# Generated by Django 4.2.1 on 2023-05-27 17:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Масса груза')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incoming_cargos', to='location.location', verbose_name='Куда груз отправлен')),
                ('pick_up', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outcoming_cargos', to='location.location', verbose_name='Откуда груз отправлен')),
                ('vehicle', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='inner_cargos', to='vehicle.vehicle', verbose_name='Машина, на которой едет груз')),
            ],
        ),
    ]
