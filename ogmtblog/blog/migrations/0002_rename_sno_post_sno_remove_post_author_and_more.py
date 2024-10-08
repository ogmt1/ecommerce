# Generated by Django 5.0.6 on 2024-08-27 18:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Sno',
            new_name='sno',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=130, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Anonymous', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
