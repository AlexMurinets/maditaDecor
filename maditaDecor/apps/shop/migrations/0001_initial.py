# Generated by Django 3.1.5 on 2021-01-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('img', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
            ],
        ),
    ]
