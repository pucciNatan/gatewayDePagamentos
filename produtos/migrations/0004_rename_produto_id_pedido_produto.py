# Generated by Django 5.1.1 on 2024-10-09 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_rename_produto_pedido_produto_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='produto_id',
            new_name='produto',
        ),
    ]
