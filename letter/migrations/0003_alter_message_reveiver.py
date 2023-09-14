# Generated by Django 4.2 on 2023-09-14 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('letter', '0002_contact_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reveiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reveiver_user', to=settings.AUTH_USER_MODEL, verbose_name='Reveiver'),
        ),
    ]