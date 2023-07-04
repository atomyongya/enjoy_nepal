# Generated by Django 4.2.2 on 2023-07-04 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DetailInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_info_title', models.CharField(max_length=2000)),
                ('detail_info_sentence', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_title', models.CharField(max_length=100)),
                ('detail_image', models.ImageField(upload_to='images/detail')),
                ('price_title', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=1000)),
                ('actual_price', models.CharField(blank=True, max_length=1000, null=True)),
                ('customer_service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_service_data', to='app.customerservicemodel')),
                ('detail_info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='detail_info_data', to='app.detailinfomodel')),
            ],
        ),
        migrations.CreateModel(
            name='ItinaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinary_info_title', models.CharField(max_length=2000)),
                ('itinary_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularDestinationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('image_path', models.ImageField(upload_to='images/home/popular_destination/')),
                ('popular_destination_detail', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.detailmodel')),
            ],
        ),
        migrations.CreateModel(
            name='KathmanduTourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('image_path', models.ImageField(upload_to='images/home/kathmandu_tour/')),
                ('kathmandu_tour_detail', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.detailmodel')),
            ],
        ),
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=40)),
                ('home_main_image', models.ImageField(upload_to='images/home')),
                ('kathmandu_tour', models.ManyToManyField(to='app.kathmandutourmodel')),
                ('popular_destination', models.ManyToManyField(to='app.populardestinationmodel')),
            ],
        ),
        migrations.AddField(
            model_name='detailmodel',
            name='itinary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='itinary_data', to='app.itinarymodel'),
        ),
    ]
