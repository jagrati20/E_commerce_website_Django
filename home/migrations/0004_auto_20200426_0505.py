# Generated by Django 3.0.5 on 2020-04-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200426_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_image',
            field=models.ImageField(null=True, upload_to='product_img'),
        ),
    ]
