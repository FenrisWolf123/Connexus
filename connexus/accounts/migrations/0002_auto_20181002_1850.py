# Generated by Django 2.1.2 on 2018-10-02 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentUser',
            new_name='User',
        ),
    ]
