# Generated by Django 3.0.4 on 2020-03-22 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200322_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='gmt_create',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
