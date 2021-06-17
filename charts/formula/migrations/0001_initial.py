# Generated by Django 3.2.4 on 2021-06-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Func',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.CharField(max_length=120, verbose_name='function')),
                ('chart_image', models.ImageField(default='chart_pics/sample_image.png', upload_to='chart_pics', verbose_name='chart_image')),
                ('interval', models.IntegerField(default=1, verbose_name='interval')),
                ('dt', models.IntegerField(default=1, verbose_name='dt')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
        ),
    ]
