# Generated by Django 3.2.8 on 2021-12-03 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_startup_is_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='tracker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startup_tracker', to=settings.AUTH_USER_MODEL),
        ),
    ]