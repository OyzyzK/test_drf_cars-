# Generated by Django 3.2.15 on 2022-09-12 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0014_auto_20220911_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentitem',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания поста'),
        ),
    ]
