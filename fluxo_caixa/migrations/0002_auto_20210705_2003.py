# Generated by Django 3.2.5 on 2021-07-05 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluxo_caixa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaspagar',
            name='status',
            field=models.BooleanField(default='false'),
        ),
        migrations.AlterField(
            model_name='contasreceber',
            name='status',
            field=models.BooleanField(default='false'),
        ),
    ]