# Generated by Django 4.1.3 on 2022-11-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Yazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=30)),
                ('soyisim', models.CharField(max_length=30)),
                ('kitaplar', models.ManyToManyField(to='app1.kitap')),
            ],
        ),
    ]
