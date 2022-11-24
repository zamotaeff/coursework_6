from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = [
        (MEMBER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30,
                                  verbose_name='Имя',
                                  null=True,
                                  blank=True)
    last_name = models.CharField(max_length=50,
                                 verbose_name='Фамилия',
                                 null=True,
                                 blank=True)
    phone = PhoneNumberField(verbose_name='Телефон',
                             unique=True,
                             null=True,
                             blank=True)
    password = models.CharField(max_length=250,
                                verbose_name='Пароль')
    role = models.CharField(max_length=10,
                            verbose_name='Роль пользователя',
                            choices=UserRoles.choices,
                            default=UserRoles.MEMBER)
    email = models.EmailField(verbose_name='email address',
                              unique=True,
                              blank=True,
                              null=True,
                              max_length=250,
                              validators=[EmailValidator(message="Домен запрещен.")])
    image = models.ImageField(upload_to='images/',
                              verbose_name='Изображение',
                              null=True,
                              blank=True)
    is_staff = models.BooleanField(verbose_name='Суперпользователь',
                                   default=False)

    USERNAME_FIELD = "email"

    def __str__(self):
        return f'{self.email}'

    class Meta:
        ordering = ()
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
