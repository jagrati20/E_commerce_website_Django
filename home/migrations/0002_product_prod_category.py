# Generated by Django 3.0.5 on 2020-04-25 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
            preserve_default=False,
        ),
    ]
