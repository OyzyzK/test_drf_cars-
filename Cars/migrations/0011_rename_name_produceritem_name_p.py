# Generated by Django 3.2.15 on 2022-09-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0010_alter_commentitem_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produceritem',
            old_name='name',
            new_name='name_p',
        ),
    ]