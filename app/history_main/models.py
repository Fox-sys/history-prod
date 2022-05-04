# -*- coding: utf-8 -*
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import choice
from string import ascii_letters


class MainUser(AbstractUser):
    """
    Main user model in project.
    Used for authentification.
    """
    middle_name = models.CharField(max_length=150, blank=True)
    email_is_hidden = models.BooleanField(default=True)
    phone = models.CharField(max_length=12, blank=True)
    phone_is_hidden = models.BooleanField(default=True)
    avatar = models.FileField(upload_to="user_avatars/", default="user_avatars/default.png")
    uploads = models.ManyToManyField("SolderPost", blank=True)
    uploads_amount = models.PositiveIntegerField(default=0)
    is_moderator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    secret_key = models.CharField(max_length=20, default=''.join(choice(ascii_letters) for i in range(20)))

    def __str__(self):
        return f"{self.id} - {self.username} {self.last_name} {self.first_name} {self.uploads_amount}"

    def get_absolute_url(self):
        return f'/profiles/{self.id}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class SolderPost(models.Model):
    """
    Model for representation post with Solders
    """
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    desc = models.TextField()
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    is_alive = models.BooleanField(default=False)
    photo = models.FileField(upload_to="solder_photos/")
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f"{self.id} - {self.last_name} {self.first_name} {self.is_alive}"

    def get_absolute_url(self):
        return f'/solders/{self.id}'

    class Meta:
        verbose_name = "Солдат"
        verbose_name_plural = "Солдаты"


class Exhibit(models.Model):
    """
    Model for representation museum exhibits
    """
    name = models.CharField(max_length=150)
    desc = models.TextField()
    image = models.FileField(upload_to="museum_photos")
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    def get_absolute_url(self):
        return f'/exhibits/{self.id}'

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"


class BadWord(models.Model):
    """
        Words that shouldn't be on the site
    """
    word = models.CharField("Слово", max_length=150)

    def __str__(self):
        # return f'{self.word}'.encode('windows-1251').decode('utf-8') # if using windows
        return f'{self.word}'

    class Meta:
        verbose_name = "Плохое слово"
        verbose_name_plural = "Плохие слова"

    def __unicode__(self):
        return self.word


class Tag(models.Model):
    tag = models.CharField('Тэг', max_length=100)

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class OutDoorSchool(models.Model):
    name = models.CharField('Название', max_length=150)

    def get_absolute_url(self):
        return f'/out_door_school/{self.id}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'выездная школа'
        verbose_name_plural = 'выездные школы'


class Image(models.Model):
    outdoor_school = models.ForeignKey('OutDoorSchool', related_name='images', on_delete=models.CASCADE)
    image = models.FileField(upload_to="outdoor_school")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'картинка для выездной школы'
        verbose_name_plural = 'картинки для выездной школы'


class Teacher(models.Model):
    full_name = models.CharField('Имя', max_length=1000)
    education = models.CharField('Образование', max_length=1000)
    access = models.CharField('Должность', max_length=150)
    method_union = models.CharField('Администрация/МетодОбъединение', max_length=300)
    subject = models.CharField('Преподаваемые дисциплины', max_length=150)
    qualification = models.CharField('Квалификация', max_length=150)
    qualification_data = models.TextField(
        'Данные о повышении квалификации (за последние 3 года!) (тема, организация, '
        'год)',
    )
    ranks = models.CharField('Звания/награды', max_length=150, blank=True, null=True)
    general_experience_years = models.IntegerField('Количество общих полных лет', blank=True, null=True)
    general_year_since = models.IntegerField('общее с какого года', blank=True, null=True)
    ped_experience_years = models.IntegerField('Количество педогогических полных лет', blank=True, null=True)
    ped_year_since = models.IntegerField('педогогический с какого года', blank=True, null=True)
    in_our_school_since = models.IntegerField('В нашей школе с', blank=True, null=True)
    image = models.FileField(upload_to='teachers', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'
