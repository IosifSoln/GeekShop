# Generated by Django 3.2 on 2021-07-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
