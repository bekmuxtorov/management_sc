# Generated by Django 4.2 on 2023-09-13 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_subjects_studentuser_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'District', 'verbose_name_plural': '5. District'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': '4. Regions'},
        ),
        migrations.AlterModelOptions(
            name='studentuser',
            options={'verbose_name': 'StudentUser', 'verbose_name_plural': '3. StudentUsers'},
        ),
        migrations.AlterModelOptions(
            name='teacheruser',
            options={'verbose_name': 'TeacherUser', 'verbose_name_plural': '2. TeacherUsers'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': '1. Users'},
        ),
    ]
