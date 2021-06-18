# Generated by Django 2.2.12 on 2021-06-18 14:01

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('even_gamble_practice', '0022_auto_20210615_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cq1_3',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Winning: 25 percent; Losing: 75 percent'], [2, 'Winning: 40 percent; Losing: 60 percent'], [3, 'Winning: 50 percent; Losing: 50 percent']], null=True),
        ),
    ]
