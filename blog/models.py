from django.db import models
from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser,UserManager


class UserManager(UserManager):
    pass

class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    class Meta:
        verbose_name = verbose_name_plural = _('アカウント')

class Category(models.Model):
    name = models.CharField(
    default='',
    max_length=255,
    blank=False,
    null=False,
    unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = _('カテゴリー')


class Tag(models.Model):
    name = models.CharField(
        default='',
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = _('タグ')

from django.urls import reverse_lazy

class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False,
        verbose_name="作成日",
        )

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
        verbose_name="最終更新日",
        )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="タイトル",
        )
    body = models.TextField(
        blank=True,
        null=True,
        verbose_name="本文",
        )

    image = models.ImageField(
        upload_to='images',
        blank=True,
        null=True,
        verbose_name="画像",
        )


    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="カテゴリ",
        )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="タグ",
        )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])

    class Meta:
        verbose_name = verbose_name_plural = _('投稿')
