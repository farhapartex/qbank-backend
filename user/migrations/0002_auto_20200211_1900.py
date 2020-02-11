# Generated by Django 3.0.3 on 2020-02-11 19:00

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.IntegerField(blank=True, null=True, verbose_name='Height'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, height_field='height', max_length=500, null=True, upload_to=user.models.image_upload_path, verbose_name='Image', width_field='width'),
        ),
        migrations.AddField(
            model_name='user',
            name='width',
            field=models.IntegerField(blank=True, null=True, verbose_name='Width'),
        ),
    ]
