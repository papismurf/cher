# Generated by Django 2.2.5 on 2019-10-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0108_auto_20191003_0422")]

    operations = [
        migrations.AlterField(
            model_name="productvariant",
            name="sku",
            field=models.CharField(max_length=255, unique=True),
        )
    ]