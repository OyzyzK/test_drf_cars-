# Generated by Django 4.1.1 on 2022-09-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0008_alter_commentitem_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentitem',
            name='comment',
            field=models.CharField(max_length=250, verbose_name='Комментарий:'),
        ),
    ]