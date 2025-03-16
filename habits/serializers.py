from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import RelatedHabitOrRewordValidator, CheckLeadTimeValidator, \
    IsPleasantNotRelatedHabitOrRewordValidator, RelatedHabitNotPleasantValidator


class HabitSerializer(ModelSerializer):
    """
    Сериализатор вывода привычки
    """
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RelatedHabitOrRewordValidator(field_1="linked_habit", field_2="reward"),
            CheckLeadTimeValidator(field="time_to_done"),
            RelatedHabitNotPleasantValidator(field_1="linked_habit"),
            IsPleasantNotRelatedHabitOrRewordValidator(field_1="is_nice_habit", field_2="linked_habit", field_3="reward")
        ]