# Generated by Django 3.2.8 on 2021-12-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20211203_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='inculcation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='startup',
            name='ip',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='startup',
            name='problem',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='startup',
            name='scaling',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='startup',
            name='solution',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
