from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    STATUSES = (
        (0, 'нет ТС'),
        (1, 'в работе'),
        (2, 'ждем СП'),
        (3, 'исполнено'),
    )
    # user = None
    name = models.CharField(
        _('Заявка'),
        max_length=255,
    )
    signed = models.DateField(
        _('Дата подписи'),
    )
    # customer = None
    conclusion = models.CharField(
        _('Заключение СП'),
        max_length=255,
        blank=True, null=True,
    )
    conclusion_date = models.DateField(
        _('Дата подписи СП'),
        blank=True, null=True,
    )
    ready = models.CharField(
        _('Исполнено'),
        max_length=255,
        blank=True, null=True,
    )
    ready_date = models.DateField(
        _('Дата подписи исх.'),
        blank=True, null=True,
    )
    status = models.PositiveIntegerField(
        _('Статус'),
        choices=STATUSES,
        default=0,
    )
    info = models.TextField(
        _('Описание'),
        blank=True, null=True,
    )


    def __str__(self):
        return f'{self.name} от {self.signed}'


    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')