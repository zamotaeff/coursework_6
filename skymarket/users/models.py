from django.contrib.auth.base_user import BaseUserManager
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


class UserManager(BaseUserManager):
    """
    функция создания пользователя — в нее мы передаем обязательные поля
    """

    def create_user(self, email, first_name, last_name, phone, role, password=None, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role="admin",
            is_admin=True
        )

        user.save(using=self._db)
        return user


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
    is_active = models.BooleanField(verbose_name='Активный',
                                    default=False)
    is_admin = models.BooleanField(verbose_name='Суперпользователь',
                                   default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        ordering = ()
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
