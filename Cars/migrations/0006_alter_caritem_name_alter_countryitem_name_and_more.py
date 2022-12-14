# Generated by Django 4.1.1 on 2022-09-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0005_alter_commentitem_email_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caritem',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название машины'),
        ),
        migrations.AlterField(
            model_name='countryitem',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название страны'),
        ),
        migrations.AlterField(
            model_name='produceritem',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название производителя'),
        ),
    ]
