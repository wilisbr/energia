# Generated by Django 3.2.12 on 2022-05-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geracao', '0020_faturamento_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='faturamento',
            name='novo',
            field=models.BooleanField(default=True),
        ),
    ]