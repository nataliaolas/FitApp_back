from django.db.models.query import QuerySet
from .models import Exercise, ExerciseEquipment, ExerciseInWorkout, ExerciseStep, FavouriteExercise, FavouriteWorkoutPlan, FavouriteWorkoutSession, MuscleGroup, UserWorkoutPlan, UserWorkoutSession, WorkoutPlan, WorkoutSession
import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import timedelta

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
            exercise_equipment = validated_data['exercise_equipment'],
            author = validated_data['author']
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
    exercise_in_workout = ExerciseInWorkoutSerializer(many=True)
    class Meta:
        model = WorkoutSession
        fields = '__all__'

    def create(self, validated_data):
        print('\n****************\n')
        print(validated_data)
        print('\n****************\n')
        new_workout_session =WorkoutSession.objects.create(
            name = validated_data['name'],
            picture = validated_data['picture'],
            time_of_workout = validated_data['time_of_workout'],
        )
        new_workout_session.trained_muscles.set(validated_data['trained_muscles'])
        new_workout_session.save()
        if validated_data['exercise_in_workout']:
            for new_exercise_in_workout in validated_data['exercise_in_workout']:
                exercise_in_workout_create = ExerciseInWorkout.objects.create(
                    exercise=new_exercise_in_workout['exercise'],
                    workout_session=new_workout_session,
                    load_range=new_exercise_in_workout['load_range'],
                    min_repetitions=new_exercise_in_workout['min_repetitions'],
                    max_repetitions=new_exercise_in_workout['max_repetitions'],
                    number_of_sets=new_exercise_in_workout['number_of_sets'],
                    rest_between_sets=new_exercise_in_workout['rest_between_sets'],
                    rest_after_exercise=new_exercise_in_workout['rest_after_exercise']
                )


        return new_workout_session

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

class USerWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutPlan
        fields = '__all__'

    def create(self, validated_data):
        print("\n***************************")
        print("VALIDATED DATA")
        print(validated_data)
        print("\n***************************")
        user = validated_data['user']
        workout_plan = validated_data['workout_plan']
        start_date = validated_data['start_date']
        end_date = start_date + timedelta(days=workout_plan.duration_in_days)
        user_workout_plan = UserWorkoutPlan.objects.create(
            start_date=start_date,
            end_date=end_date,
            user=user,
            workout_plan=workout_plan
        )
        session_date = start_date
        workout_sessions = workout_plan.workout_sessions.all()
        workout_session_counter =0
        for i in range(workout_plan.duration_in_days):
            if workout_session_counter > len(workout_sessions)-1:
                workout_session_counter = 0
            session_date += timedelta(days=i)
            if  i % (workout_plan.workout_session_row+1) == 0:
                pass
            elif workout_plan.workout_session_row == 2 and i%7 == 0:
                pass
            else:
                UserWorkoutSession.objects.create(
                    workout_plan=user_workout_plan,
                    workout_session=workout_sessions[workout_session_counter],
                    date_of_workout=session_date
                )
                workout_session_counter += 1
        
        return super().create(validated_data)


class FavouriteExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteExercise
        fields = '__all__'

class FavouriteWorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteWorkoutSession
        fields = '__all__'

class FavouriteWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteWorkoutPlan
        fields = '__all__'
