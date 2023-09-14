# Generated by Django 4.2 on 2023-09-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_district_options_alter_region_options_and_more'),
        ('study_center', '0004_delete_message_alter_day_options_alter_room_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectgroup',
            name='students',
            field=models.ManyToManyField(related_name='subject_groups', to='account.studentuser'),
        ),
    ]
