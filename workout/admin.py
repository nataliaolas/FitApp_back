from django.contrib import admin
from workout.models import (
    MuscleGroup,
    ExerciseStep,
    ExerciseEquipment,
    Exercise,
    UserWorkoutPlan, UserWorkoutSession, WorkoutPlan,
    WorkoutSession,
    ExerciseInWorkout,
)


class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ("name")


class ExerciseStepInline(admin.TabularInline):
    model = ExerciseStep
    extra = 3


class ExerciseEquipmentAdmin(admin.ModelAdmin):
    list_display = ("name")


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "exercise_equipment")
    inlines = [ExerciseStepInline]


class ExerciseInWorkoutAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'number_of_sets',
                    'rest_between_sets', 'rest_after_exercise')


class ExerciseInWorkoutInline(admin.TabularInline):
    model = ExerciseInWorkout
    extra = 3


class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ("name", "time_of_workout")
    inlines = [ExerciseInWorkoutInline]


admin.site.register(MuscleGroup)
admin.site.register(ExerciseEquipment)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WorkoutSession, WorkoutSessionAdmin)
admin.site.register(ExerciseInWorkout, ExerciseInWorkoutAdmin)
admin.site.register(WorkoutPlan)
admin.site.register(UserWorkoutSession)
admin.site.register(UserWorkoutPlan)
