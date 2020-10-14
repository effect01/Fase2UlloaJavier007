# Generated by Django 3.1.2 on 2020-10-14 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=65)),
                ('last_name', models.CharField(max_length=65)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.DeleteModel(
            name='NuevaClase',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.author'),
            preserve_default=False,
        ),
    ]