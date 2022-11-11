# Generated by Django 4.1 on 2022-11-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyerID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=300)),
                ('email', models.CharField(default='', max_length=300)),
                ('username', models.CharField(default='', max_length=300)),
                ('password', models.CharField(default='', max_length=300)),
                ('address', models.CharField(default='', max_length=1000)),
                ('payment', models.FloatField(default='1')),
            ],
        ),
    ]
