from django.contrib.auth.models import AbstractUser
from django.db import models

from api.v1.core import keygen, slug_keygen


class Seller(AbstractUser):
    client_id = models.CharField(
        max_length=256,
        unique=True,
        default=keygen()
    )
    api_key = models.CharField(
        max_length=256,
        unique=True,
        default=slug_keygen()
    )


class Etgb_of_posting(models.Model):
    posting_number = models.TextField(
        unique=True,
        default=keygen())
    etgb = models.ForeignKey(
        'Etgb',
        on_delete=models.CASCADE,
        related_name='etgb',
        verbose_name='Декларация'
    )
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='seller',
        verbose_name='Владелец деклорации',
    )

    class Meta:
        verbose_name = 'Таможенная декларация отправленной посылки'
        verbose_name_plural = 'Таможенные декларации отправленных посылок'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['posting_number', 'etgb'],
                name='uniq_etgb_of_posting'
            )
        ]

    def __str__(self):
        return f'{self.posting_number} {self.etgb}'


class Etgb(models.Model):
    number = models.TextField(
        unique=True,
        default=keygen())
    date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True,
    )
    url = models.SlugField(
        unique=True,
        default=slug_keygen())

    class Meta:
        verbose_name = 'Таможенная декларация'
        verbose_name_plural = 'Таможенные декларации'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['number', 'url'],
                name='uniq_etgb'
            )
        ]

    def __str__(self):
        return f'{self.date}'
