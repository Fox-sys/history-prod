# Generated by Django 3.1.5 on 2021-01-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_main', '0002_auto_20210126_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='avatar',
            field=models.ImageField(default='user_avatars/default.png', upload_to='user_avatars/'),
        ),
    ]
