# Generated by Django 4.0.1 on 2022-01-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_template', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Food_price',
            field=models.IntegerField(),
        ),
    ]
