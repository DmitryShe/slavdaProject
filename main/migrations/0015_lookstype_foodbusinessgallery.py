# Generated by Django 4.1.7 on 2023-05-06 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_kitchentype_alter_foodbusiness_orgfoodcoord_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LooksType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfLooks', models.CharField(max_length=100, verbose_name='Тип достопримечательности')),
            ],
            options={
                'verbose_name': 'Тип достопримечательности',
                'verbose_name_plural': 'Тип достопримечательности',
            },
        ),
        migrations.CreateModel(
            name='FoodBusinessGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование изображения')),
                ('image', models.ImageField(upload_to='FoodBusiness_gallery/%Y/%m/%d/')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FoodBusiness_images', to='main.foodbusiness')),
            ],
            options={
                'verbose_name': 'Фото из общепита',
                'verbose_name_plural': 'Фото из общепита',
            },
        ),
    ]
