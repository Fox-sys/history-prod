# Generated by Django 3.1.5 on 2021-04-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_main', '0012_auto_20210414_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='secret_key',
            field=models.CharField(default='GGwtajIaLQedXfALuexY', max_length=20),
        ),
        migrations.AddField(
            model_name='solderpost',
            name='tags',
            field=models.ManyToManyField(blank=True, to='history_main.Tag'),
        ),
    ]
