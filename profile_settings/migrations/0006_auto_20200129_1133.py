# Generated by Django 3.0.1 on 2020-01-29 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_settings', '0005_auto_20200129_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinstagramusersettings',
            old_name='prodcut_emails',
            new_name='product_emails',
        ),
    ]