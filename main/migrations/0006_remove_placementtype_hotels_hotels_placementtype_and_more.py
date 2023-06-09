# Generated by Django 4.1.7 on 2023-05-02 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_placementtype_id_placementtype_hotels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placementtype',
            name='hotels',
        ),
        migrations.AddField(
            model_name='hotels',
            name='placementType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.placementtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placementtype',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
