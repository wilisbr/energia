# Generated by Django 3.2.12 on 2022-04-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geracao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faturamento',
            name='conta_pdf',
            field=models.FileField(blank=True, null=True, upload_to='contas_pdf'),
        ),
    ]
