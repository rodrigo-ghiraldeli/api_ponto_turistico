# Generated by Django 2.2 on 2019-04-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracao', '0002_auto_20190327_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]
