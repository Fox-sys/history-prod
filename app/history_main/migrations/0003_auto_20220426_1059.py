# Generated by Django 3.1.5 on 2022-04-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_main', '0002_auto_20220426_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.FileField(default='', upload_to='outdoor_school'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='secret_key',
            field=models.CharField(default='ORhjqZePKtBFRTlECTAX', max_length=20),
        ),
    ]