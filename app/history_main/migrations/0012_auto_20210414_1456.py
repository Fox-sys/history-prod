# Generated by Django 3.1.5 on 2021-04-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_main', '0011_auto_20210304_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solderpost',
            name='creator',
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='secret_key',
            field=models.CharField(default='hTgoULXiQHgjzLzNTGxk', max_length=20),
        ),
    ]
