from .models import Exercise, ExerciseEquipment, ExerciseInWorkout, ExerciseStep, MuscleGroup, WorkoutPlan, WorkoutSession
import datetime
from django.contrib.auth.models import User
from rest_framework import serializers

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'

class ExerciseEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseEquipment
        fields = '__all__'

class ExerciseStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStep
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    steps = ExerciseStepSerializer(many=True)
    class Meta:
        model = Exercise
        fields = '__all__'
    
    def create(self, validated_data):
        new_exercise =Exercise.objects.create(
            name = validated_data['name'],
            picture = validated_data['picture'],
            public = validated_data['public'],
            description = validated_data['description'],
            exercise_equipment = validated_data['exercise_equipment']
        )
        new_exercise.muscle_groups.set(validated_data['muscle_groups'])
        new_exercise.save()
        if validated_data['steps']:
            for new_step in validated_data['steps']:
                step = ExerciseStep.objects.create(
                    step=new_step['step'],
                    exercise=new_exercise
                )
        return new_exercise
    def update(self, instance, validated_data):
        print('\n****************\n')
        print(validated_data)
        print('\n****************\n')
        instance.name = validated_data.get('name', instance.name)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.public = validated_data.get('public', instance.public)
        instance.description = validated_data.get('description', instance.description)
        instance.muscle_groups.set(validated_data.get('muscle_groups', instance.muscle_groups))
        instance.exercise_equipment = validated_data.get('exercise_equipment', instance.exercise_equipment)
        instance.save()

        existing_steps = instance.get_exercise_steps()
        steps = validated_data['steps']
        for i in range(len(existing_steps)):
            existing_steps[i].delete()
        for n_step in steps:
            new_step = ExerciseStep.objects.create(
                    step=n_step['step'],
                    exercise=instance
                )
        return instance

class ExerciseInWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInWorkout
        fields = '__all__'

class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'