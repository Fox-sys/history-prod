# Generated by Django 3.1.5 on 2022-04-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_main', '0003_auto_20220426_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000, verbose_name='Имя')),
                ('education', models.CharField(max_length=1000, verbose_name='Образование')),
                ('access', models.CharField(max_length=150, verbose_name='Должность')),
                ('method_union', models.CharField(max_length=300, verbose_name='Администрация/МетодОбъединение')),
                ('subject', models.CharField(max_length=150, verbose_name='Преподаваемые дисциплины')),
                ('qualification', models.CharField(max_length=150, verbose_name='Квалификация')),
                ('qualification_data', models.TextField(verbose_name='Данные о повышении квалификации (за последние 3 года!) (тема, организация, год)')),
                ('ranks', models.CharField(blank=True, max_length=150, null=True, verbose_name='Звания/награды')),
                ('general_experience_years', models.IntegerField(blank=True, null=True, verbose_name='Количество общих полных лет')),
                ('ped_experience_years', models.IntegerField(blank=True, null=True, verbose_name='Количество педогогических полных лет')),
                ('general_year_since', models.IntegerField(blank=True, null=True, verbose_name='общее с какого года')),
                ('ped_year_since', models.IntegerField(blank=True, null=True, verbose_name='педогогический с какого года')),
                ('in_our_school_since', models.IntegerField(blank=True, null=True, verbose_name='В нашей школе с')),
                ('image', models.FileField(blank=True, null=True, upload_to='teachers')),
            ],
            options={
                'verbose_name': 'учитель',
                'verbose_name_plural': 'учителя',
            },
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='secret_key',
            field=models.CharField(default='JBVOhcAvuxGogEEPMtVc', max_length=20),
        ),
    ]
