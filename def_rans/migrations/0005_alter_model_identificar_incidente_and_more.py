# Generated by Django 4.2.6 on 2024-05-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('def_rans', '0004_alter_model_identificar_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_identificar',
            name='incidente',
            field=models.IntegerField(choices=[[0, 'Toma las decisiones sobre como actuar'], [1, 'Lo reporta ante un directivo para obtener el plan de acción'], [2, 'Depende de un tercero que le brinda servicios de seguridad para actuar ante el incidente'], [3, 'Otro']], verbose_name='En el caso de un incidente de segurdad informática (ataque por viruso informático u otras formas) usted: '),
        ),
        migrations.AlterField(
            model_name='model_identificar',
            name='rol',
            field=models.IntegerField(choices=[[0, 'Administrativo'], [1, 'Directivo'], [2, 'Servicio'], [3, 'Sistemas/Informática/TICs'], [4, 'Soporte'], [5, 'Otro']], verbose_name='¿Cuál es su puesto/rol en su organización?'),
        ),
    ]
