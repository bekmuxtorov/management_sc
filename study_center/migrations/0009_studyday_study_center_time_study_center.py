# Generated by Django 4.2 on 2023-09-28 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_center', '0008_alter_room_teacher_alter_subjectgroup_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyday',
            name='study_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_day', to='study_center.studycenter', verbose_name='Study center'),
        ),
        migrations.AddField(
            model_name='time',
            name='study_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='times', to='study_center.studycenter', verbose_name='Study center'),
        ),
    ]
