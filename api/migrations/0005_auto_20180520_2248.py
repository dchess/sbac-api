# Generated by Django 2.0.5 on 2018-05-20 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_subgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subgroup',
            old_name='sub_group_id',
            new_name='subgroup_id',
        ),
    ]