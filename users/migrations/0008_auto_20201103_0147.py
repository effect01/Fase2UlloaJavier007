# Generated by Django 3.1.2 on 2020-11-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201103_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code_number',
            field=models.IntegerField(choices=[(56, 'CHL +56'), (54, 'ARG +54'), (55, 'BRZ +55'), (1, 'USA +1'), (57, 'COL +57')], default=56),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dateBirth',
            field=models.DateField(),
        ),
    ]
