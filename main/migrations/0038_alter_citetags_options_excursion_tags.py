# Generated by Django 4.1.7 on 2023-05-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_citetags_foodbusiness_tags_hotels_tags_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citetags',
            options={'verbose_name': 'Тэг сайта', 'verbose_name_plural': 'Тэг сайта'},
        ),
        migrations.AddField(
            model_name='excursion',
            name='tags',
            field=models.ManyToManyField(null=True, to='main.citetags', verbose_name='Тэги'),
        ),
    ]