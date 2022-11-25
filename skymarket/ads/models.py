from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(max_length=1000,
                                   null=True,
                                   blank=True)
    author = models.ForeignKey(User,
                               verbose_name='Пользователь',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    image = models.ImageField(upload_to='images/',
                              verbose_name='Изображение',
                              null=True,
                              blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    text = models.TextField(max_length=1000,
                            null=True,
                            blank=True)
    author = models.ForeignKey(User,
                               verbose_name='Пользователь',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    ad = models.ForeignKey(Ad,
                           verbose_name='Объявление',
                           on_delete=models.CASCADE,
                           null=True,
                           blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')

    class Meta:
        ordering = ()
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
