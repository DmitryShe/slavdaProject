# Generated by Django 4.1.7 on 2023-05-06 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_organizationcoordinaties_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.TextField(max_length=250, verbose_name='Адрес')),
                ('contacts', models.TextField(verbose_name='Контакты')),
                ('link', models.TextField(verbose_name='Ссылки на сайт')),
                ('workingHours', models.TextField(verbose_name='Время работы')),
                ('price', models.IntegerField(verbose_name='Средний чек')),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательность',
            },
        ),
        migrations.AlterModelOptions(
            name='organizationcoordinaties',
            options={'verbose_name': 'Координаты предприятия', 'verbose_name_plural': 'Координаты предприятий'},
        ),
        migrations.AlterModelOptions(
            name='placementtype',
            options={'verbose_name': 'Тип отеля', 'verbose_name_plural': 'Тип отеля'},
        ),
        migrations.CreateModel(
            name='ShowplacesGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование изображения')),
                ('image', models.ImageField(upload_to='Showplaces_gallery/%Y/%m/%d/')),
                ('showplaces', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Showplaces_images', to='main.showplaces')),
            ],
            options={
                'verbose_name': 'Фото достопримечательности',
                'verbose_name_plural': 'Фото достопримечательности',
            },
        ),
        migrations.AddField(
            model_name='showplaces',
            name='showPlacesCoord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.organizationcoordinaties'),
        ),
        migrations.AddField(
            model_name='showplaces',
            name='showplacesType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.showplacestype'),
        ),
    ]
