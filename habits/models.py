from django.db import models

from users.models import User


class Habit(models.Model):
    """
    Модель привычки
    """
    PERIODS = (
        ('day', 'Ежедневно'),
        ('week', 'Еженедельно'),
    )

    owner=models.ForeignKey(User, verbose_name='Создатель привычки', null=True, blank=True, on_delete=models.CASCADE)
    place = models.CharField(max_length=500, verbose_name='Место выполнения привычки', null=True, blank=True)
    start_time = models.DateTimeField(verbose_name='Время, когда необходимо выполнять привычку', null=True, blank=True)
    action = models.CharField(
        max_length=300,
        verbose_name='Действие, которое представляет собой привычка',
        null=True,
        blank=True
    )
    is_nice_habit = models.BooleanField(verbose_name='Признак приятной привычки')
    linked_habit = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Связанная привычка',
        related_name='linked_habits',
        null=True,
        blank=True
    )
    period = models.CharField(
        max_length=4,
        choices=PERIODS,
        verbose_name='Периодичность',
        null=True,
        blank=True
    )
    reward = models.CharField(
        max_length=300,
        verbose_name='Вознаграждение',
        null=True,
        blank=True
    )
    time_to_done = models.PositiveIntegerField(verbose_name='Время на выполнение (в минутах)', null=True, blank=True)
    is_public = models.BooleanField(verbose_name='Публичная привычка')

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
