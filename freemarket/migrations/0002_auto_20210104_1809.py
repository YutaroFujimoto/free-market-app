# Generated by Django 3.1.3 on 2021-01-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freemarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture_1',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture_2',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture_3',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture_4',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
