from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Etgb_of_posting(models.Model):
    posting_number = models.TextField(unique=True, max_length=None)
    etgb = models.ForeignKey(
        'Etgb',
        on_delete=models.CASCADE,
        related_name='etgb',
        verbose_name='Декларация'
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
        return self.posting_number


class Etgb(models.Model):
    number = models.TextField(unique=True)
    date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True,
    )
    url = models.SlugField(unique=True)

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
        return self.number
