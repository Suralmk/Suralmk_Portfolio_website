# Generated by Django 5.0.2 on 2024-02-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0002_alter_work_work_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
