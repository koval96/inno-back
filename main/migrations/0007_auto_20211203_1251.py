# Generated by Django 3.2.8 on 2021-12-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211203_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='startup',
            name='is_strong',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='website_url',
            field=models.URLField(blank=True),
        ),
    ]