# Generated by Django 3.2.12 on 2022-05-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geracao', '0014_alter_faturamento_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.TextField(default='Cliente Sem Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.TextField(blank=True, null=True),
        ),
    ]