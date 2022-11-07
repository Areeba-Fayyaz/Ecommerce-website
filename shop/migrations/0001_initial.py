# Generated by Django 4.1 on 2022-11-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(default='', max_length=300)),
                ('productType', models.CharField(default='', max_length=300)),
                ('description', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default='1')),
                ('productImage', models.ImageField(default='', upload_to='myShop/Images')),
            ],
        ),
    ]
