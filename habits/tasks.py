import datetime

import pytz
from celery import shared_task

from config import settings
from habits.models import Habit
from habits.services import send_telegram_message

PERIOD_TIMEDELTA = {
    'day': datetime.timedelta(days=1),
    'week': datetime.timedelta(weeks=1)
    }

@shared_task
def check_habits():
    """
    Периодическая задача
    """
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.datetime.now(zone)
    habits = Habit.objects.filter(owner__tg_nick__isnull=False)
    for habit in habits:
        if habit.start_time <= now:
            user_tg = habit.owner.tg_nick
            if habit.place:
                message = f"Пришло время {habit.action} в {habit.place}"
            else:
                message = f"Пришло время {habit.action}"
            send_telegram_message(user_tg, message)
            habit.start_time += PERIOD_TIMEDELTA
