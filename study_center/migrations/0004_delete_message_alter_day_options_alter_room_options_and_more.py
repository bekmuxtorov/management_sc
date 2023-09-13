# Generated by Django 4.2 on 2023-09-13 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_center', '0003_day_message_room_studyday_time_subjectgroup_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AlterModelOptions(
            name='day',
            options={'verbose_name': 'Day', 'verbose_name_plural': '5.Days'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Room', 'verbose_name_plural': '7.Rooms'},
        ),
        migrations.AlterModelOptions(
            name='studycenter',
            options={'verbose_name': 'Study center', 'verbose_name_plural': '1.Study centers'},
        ),
        migrations.AlterModelOptions(
            name='studyday',
            options={'verbose_name': 'StudyDay', 'verbose_name_plural': '6.Study Days'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Subject', 'verbose_name_plural': '3.Subject'},
        ),
        migrations.AlterModelOptions(
            name='subjectgroup',
            options={'verbose_name': 'Study Group', 'verbose_name_plural': '2.Study centers'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': 'Time', 'verbose_name_plural': '4.Times'},
        ),
        migrations.AlterField(
            model_name='studyday',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_day', to='study_center.day', verbose_name='Day'),
        ),
    ]
