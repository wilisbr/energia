# Generated by Django 3.2.12 on 2022-05-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geracao', '0007_auto_20220503_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='faturamento',
            name='referencia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
