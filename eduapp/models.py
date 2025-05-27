from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ProgramInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    my_name = models.CharField(max_length=100)
    my_photo = models.ImageField(upload_to='photos/')
    my_email = models.EmailField()
    my_phone = models.CharField(max_length=20)
    head_name = models.CharField(max_length=100)
    head_photo = models.ImageField(upload_to='photos/')
    head_email = models.EmailField()
    manager_name = models.CharField(max_length=100)
    manager_photo = models.ImageField(upload_to='photos/')
    manager_email = models.EmailField()


class Student(models.Model):
    GENDER_CHOICES = [('М', 'Мужской'), ('Ж', 'Женский')]

    name = models.CharField(max_length=255, verbose_name='ФИО')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name='Пол')
    email = models.EmailField(verbose_name='Электронная почта')
    course = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        verbose_name='Курс'
    )
    average_score = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Средний балл'
    )
