# Generated by Django 3.2.12 on 2022-05-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geracao', '0022_remove_faturamento_novo'),
    ]

    operations = [
        migrations.AddField(
            model_name='faturamento',
            name='distribuidora',
            field=models.TextField(default='cemig'),
            preserve_default=False,
        ),
    ]
