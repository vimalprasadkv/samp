# Generated by Django 3.2 on 2022-11-08 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samppleApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cu_user',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='cu_user',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='cu_user',
            old_name='username',
            new_name='user_name',
        ),
    ]
