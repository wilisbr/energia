# Generated by Django 3.2.12 on 2022-04-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geracao', '0004_auto_20220407_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='faturamento',
            name='energia_da_concessionaria',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]