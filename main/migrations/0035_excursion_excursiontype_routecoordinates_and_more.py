# Generated by Django 4.1.7 on 2023-05-15 15:15

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_citeinformations_organizationdeveloperimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название экскурсии')),
                ('description', froala_editor.fields.FroalaField()),
                ('route', froala_editor.fields.FroalaField()),
                ('timeStart', models.CharField(max_length=20, verbose_name='Время начала экскурсии')),
                ('exDuration', models.CharField(max_length=20, verbose_name='Продолжительность экскурсии')),
                ('tourOperator', models.CharField(max_length=100, verbose_name='Организатор')),
                ('link', models.CharField(max_length=100, verbose_name='Ссылка на экскурсию, организатора')),
                ('price', models.IntegerField(verbose_name='Цена экскурсии')),
            ],
            options={
                'verbose_name': 'Экскурсии',
                'verbose_name_plural': 'Экскурсии',
            },
        ),
        migrations.CreateModel(
            name='ExcursionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfexcursion', models.CharField(max_length=100, verbose_name='Вид экскурсии')),
            ],
            options={
                'verbose_name': 'Вид экскурсии',
                'verbose_name_plural': 'Вид экскурсии',
            },
        ),
        migrations.CreateModel(
            name='RouteCoordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название точки')),
                ('routeX', models.FloatField(verbose_name='координата X')),
                ('routeY', models.FloatField(verbose_name='координата Y')),
                ('excursion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ex_route', to='main.excursion', verbose_name='экскурсия')),
            ],
        ),
        migrations.CreateModel(
            name='ExcursionGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование изображения')),
                ('image', models.ImageField(upload_to='Excursion_gallery/%Y/%m/%d/')),
                ('excursion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Excursion_images', to='main.excursion', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'Фото экскурсии',
                'verbose_name_plural': 'Фото экскурсии',
            },
        ),
        migrations.AddField(
            model_name='excursion',
            name='excursionType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.excursiontype', verbose_name='вид экскурсии'),
        ),
    ]
