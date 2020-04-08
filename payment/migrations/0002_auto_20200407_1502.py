# Generated by Django 3.0.4 on 2020-04-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'SUCCESSFUL'), (1, 'FAILED'), (2, 'IN_PROGRESS'), (3, 'REFUND')], default=0),
        ),
    ]