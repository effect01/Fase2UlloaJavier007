# Generated by Django 3.1.2 on 2020-11-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201021_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(default='https://image.freepik.com/vector-gratis/revista-vacia-portada-album-o-libro_150973-63.jpg', verbose_name='Image Address'),
        ),
        migrations.AlterField(
            model_name='post',
            name='previewContent',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
