# Generated by Django 3.2.3 on 2021-07-18 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0018_auto_20210629_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='volumes',
            new_name='chapters',
        ),
    ]
