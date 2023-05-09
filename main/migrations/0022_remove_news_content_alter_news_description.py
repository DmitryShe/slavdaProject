# Generated by Django 4.1.7 on 2023-05-09 12:53

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
    ]