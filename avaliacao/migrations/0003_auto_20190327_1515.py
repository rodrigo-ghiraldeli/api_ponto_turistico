# Generated by Django 2.1.7 on 2019-03-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0002_auto_20190327_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
