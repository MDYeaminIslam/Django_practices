# Generated by Django 4.1.5 on 2023-03-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('re_password', models.CharField(max_length=50)),
                ('laptop', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('about', models.CharField(max_length=50)),
                ('textarea', models.CharField(max_length=50)),
                ('checkbox', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('ssd', models.DecimalField(decimal_places=2, max_digits=3)),
                ('youtube_channel', models.BooleanField(max_length=50)),
            ],
        ),
    ]
