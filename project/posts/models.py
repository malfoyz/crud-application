from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """Модель блог-поста"""

    name = models.CharField(
        max_length=100,
        verbose_name=_('Название'),
    )
    content = models.TextField(
        verbose_name=_('Текст'),
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        verbose_name=_('Фото'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата обновления'),
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        related_name='posts',
        related_query_name='post',
        verbose_name=_('Автор'),
    )
    category = models.ForeignKey(
        to='Category',
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='posts',
        related_query_name='post',
        verbose_name=_('Категория'),
    )
    tag = models.ManyToManyField(   # tags
        to='Tag',
        blank=True,
        verbose_name=_('Теги'),
        related_name='posts',
        related_query_name='post',
    )

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')
        ordering = ('-updated_at',)

    def get_absolute_url(self) -> str:
        return reverse('posts:get_post', kwargs={'id': self.pk})

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель категории"""

    name = models.CharField(
        max_length=50,
        verbose_name=_('Название'),
    )

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    """Модель тега"""

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_('Название'),
    )

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    """Модель комментария"""

    text = models.TextField(
        verbose_name=_('Текст'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата обновления'),
    )
    post = models.ForeignKey(
        to='Post',
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
        verbose_name=_('Пост'),
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
        verbose_name=_('Пользователь'),
    )

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.created_at