# Generated by Django 4.2.7 on 2023-11-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_carro_anofabricacao_alter_carro_modelo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='imgUrl',
            field=models.CharField(default=3, max_length=200),
            preserve_default=False,
        ),
    ]
