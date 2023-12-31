# Generated by Django 3.2.13 on 2023-07-05 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230705_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thingstodomodel',
            name='culture_tour_details',
        ),
        migrations.RemoveField(
            model_name='thingstodomodel',
            name='food_tour_details',
        ),
        migrations.RemoveField(
            model_name='thingstodomodel',
            name='treak_details',
        ),
        migrations.AddField(
            model_name='thingstodomodel',
            name='culture_tour',
            field=models.ManyToManyField(related_name='culture_tour', to='app.CultureTourModel'),
        ),
        migrations.AddField(
            model_name='thingstodomodel',
            name='food_tour',
            field=models.ManyToManyField(related_name='food_tour', to='app.FoodTourModel'),
        ),
        migrations.AddField(
            model_name='thingstodomodel',
            name='treak',
            field=models.ManyToManyField(related_name='treak', to='app.TreakModel'),
        ),
        migrations.DeleteModel(
            name='ThingsToDoDetailModel',
        ),
    ]
