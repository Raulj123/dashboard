# Generated by Django 4.2.4 on 2023-08-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0004_userexpense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexpense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
    ]
