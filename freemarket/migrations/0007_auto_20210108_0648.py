# Generated by Django 3.1.3 on 2021-01-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freemarket', '0006_auto_20210108_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
