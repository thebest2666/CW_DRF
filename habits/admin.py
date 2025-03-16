from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('owner', 'time_to_done', 'action',)
    search_fields = ('owner',)
