# Generated by Django 3.2.7 on 2021-10-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_pedido_qtd_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]