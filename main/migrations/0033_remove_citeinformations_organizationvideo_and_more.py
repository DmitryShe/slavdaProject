# Generated by Django 4.1.7 on 2023-05-14 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_hotels_placementtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citeinformations',
            name='organizationVideo',
        ),
        migrations.RemoveField(
            model_name='citeinformations',
            name='organizationVideoContentDescription',
        ),
        migrations.RemoveField(
            model_name='citeinformations',
            name='organizationVideoContentHeader',
        ),
        migrations.DeleteModel(
            name='OrganizationGallery',
        ),
    ]
