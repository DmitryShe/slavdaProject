# Generated by Django 4.1.7 on 2023-05-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_foodbusiness_id_alter_foodbusiness_orgfoodcoord'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationcoordinaties',
            name='title',
            field=models.CharField(default=1, max_length=200, verbose_name='Наименование'),
            preserve_default=False,
        ),
    ]
