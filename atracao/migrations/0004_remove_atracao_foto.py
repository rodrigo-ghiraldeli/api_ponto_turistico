# Generated by Django 2.2 on 2019-04-02 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atracao', '0003_atracao_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atracao',
            name='foto',
        ),
    ]
