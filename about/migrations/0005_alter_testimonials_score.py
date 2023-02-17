# Generated by Django 4.1.5 on 2023-01-19 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_testimonials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Awful'), (2, 'Bad'), (3, 'Regular'), (4, 'Good'), (5, 'Exelent')], default=5),
        ),
    ]
