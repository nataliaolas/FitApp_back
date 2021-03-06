import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CookingStep, Diet, DietDay, DietType, FavouriteDiet, FavouriteMeal, IngredientPortion, Meal, UserDiet, UserDietDay


class CookingStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingStep
        fields = '__all__'

class IngredientPortionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientPortion
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientPortionSerializer(many=True)
    steps = CookingStepSerializer(many=True)
    class Meta:
        model = Meal
        fields = '__all__'

    def create(self, validated_data):
        print("\n\n ****************** \n")
        print(validated_data)
        print("\n\n ****************** \n")
        new_meal = Meal.objects.create(
            name=validated_data['name'],
            picture=validated_data['picture'],
            description=validated_data['description'],
            meal_type=validated_data['meal_type'],
            cooking_time=validated_data['cooking_time'],
            kcal=validated_data['kcal'],
            proteins=validated_data['proteins'],
            fats=validated_data['fats'],
            carbohydrates=validated_data['carbohydrates'],
            author=validated_data['author']
        )
        if validated_data['ingredients']:
            for new_ingredient in validated_data['ingredients']:
                ingredient = IngredientPortion.objects.create(
                    ingredient=new_ingredient['ingredient'],
                    portion=new_ingredient['portion'],
                    meal=new_meal
                )
        if validated_data['steps']:
            for new_step in validated_data['steps']:
                step = CookingStep.objects.create(
                    step=new_step['step'],
                    meal=new_meal
                )
        return new_meal
    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.meal_type = validated_data.get('meal_type', instance.meal_type)
        instance.cooking_time = validated_data.get('cooking_time', instance.cooking_time)
        instance.kcal = validated_data.get('kcal', instance.kcal)
        instance.proteins = validated_data.get('proteins', instance.proteins)
        instance.fats = validated_data.get('fats', instance.fats)
        instance.carbohydrates = validated_data.get('carbohydrates', instance.carbohydrates)
        instance.save()
        ingredients = validated_data['ingredients']
        existing_ingredients = instance.ingredients.all()
        #maybe it's better to just clear existing_ingredients/steps(delete objects) and then create objects based on ingredients/steps
        if len(ingredients) == len(existing_ingredients):
            for i in range(len(ingredients)):
                if ingredients[i]['ingredient'] != existing_ingredients[i].ingredient:
                    existing_ingredients[i].ingredient = ingredients[i]['ingredient']
                    if ingredients[i]['portion'] != existing_ingredients[i].portion:
                        existing_ingredients[i].portion = ingredients[i]['portion']
                    existing_ingredients[i].save()
                else:
                    if ingredients[i]['portion'] != existing_ingredients[i].portion:
                        existing_ingredients[i].portion = ingredients[i]['portion']
                        existing_ingredients[i].save()

        elif len(ingredients) < len(existing_ingredients):
            for i in range(len(ingredients)):
                existing_ingredients[i].ingredient = ingredients[i]['ingredient']
                existing_ingredients[i].portion = ingredients[i]['portion']
                existing_ingredients[i].save()
            for i in range(len(existing_ingredients)-(len(existing_ingredients)-len(ingredients)), len(existing_ingredients)):
                existing_ingredients[i].delete()
        else:
            for i in range(len(existing_ingredients)):
                existing_ingredients[i].ingredient = ingredients[i]['ingredient']
                existing_ingredients[i].portion = ingredients[i]['portion']
            for i in range(len(ingredients)-(len(ingredients)-len(existing_ingredients)), len(ingredients)):
                new_ingredient = IngredientPortion.objects.create(
                    ingredient=ingredients[i]['ingredient'],
                    portion=ingredients[i]['portion'],
                    meal=instance
                )        
        steps = validated_data['steps']
        existing_steps = instance.steps.all()
        print("\n ********** \n")
        print(len(steps))
        print(len(existing_steps))
        print("\n ********** \n")
        if len(steps) == len(existing_steps):
            for i in range(len(steps)):
                if steps[i]['step'] != existing_steps[i].step:
                    existing_steps[i].step = steps[i]['step']
                    existing_steps[i].save()
        elif len(steps) < len(existing_steps):
 
            for i in range(len(steps)):
                existing_steps[i].step = steps[i]['step']
                existing_steps[i].save()
            for i in range(len(existing_steps)-(len(existing_steps)-len(steps)), len(existing_steps)):
                existing_steps[i].delete()
        else:
            for i in range(len(existing_steps)):
                existing_steps[i].step = steps[i]['step']
                existing_steps[i].save()
            for i in range(len(steps)-(len(steps)-len(existing_steps)), len(steps)):
                new_step = CookingStep.objects.create(
                    step=steps[i]['step'],
                    meal=instance
                )
        return instance

class DietTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietType
        fields = '__all__'

class DietDaySerializer(serializers.ModelSerializer):
    # meals = MealSerializer(many=True)
    class Meta:
        model = DietDay
        fields = '__all__'

class DietSerializer(serializers.ModelSerializer):
    # diet_days = DietDaySerializer(many=True)
    class Meta:
        model = Diet
        fields = '__all__'
    
    def update(self, instance, validated_data):
        print(validated_data)
        return super().update(instance, validated_data)


class UserDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDiet
        fields = '__all__'

    def create(self, validated_data):
        print("\n***************************")
        print("VALIDATED DATA")
        print(validated_data)
        print("\n***************************")
        user = validated_data['user']
        diet = validated_data['diet']
        start_date = validated_data['start_date']
        end_date = start_date + datetime.timedelta(days=diet.duration_in_days)
        user_diet_plan = UserDiet.objects.create(
            start_date=start_date,
            end_date=end_date,
            user=user,
            diet=diet
        )
        eating_date = start_date
        diet_days = diet.diet_days.all()

        for i in range(diet.duration_in_days):
            print("\n***************************")
            print("DIET DAY OD I")
            print(diet_days[i])
            print("\n***************************")
            UserDietDay.objects.create(
                diet=user_diet_plan,
                diet_day=diet_days[i],
                diet_day_date=eating_date
            )
            eating_date = eating_date + datetime.timedelta(days=i)
    
        return user_diet_plan


    def validate(self, data):
        print("\n***************************")
        print(data['start_date'])
        print(datetime.date.today())
        print("\n***************************")
        if data['start_date'] < datetime.date.today():
            raise serializers.ValidationError({"start_date" : 'Data rozpoczecia nie moze byc z przeszlosci'})
        
        return super().validate(data)


class UserDietDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDietDay
        fields = '__all__'

class FavouriteMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteMeal
        fields = '__all__'

class FavouriteDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteDiet
        fields = '__all__'

class DietDayWithMealNamesSerializer(serializers.ModelSerializer):
    meals = serializers.StringRelatedField(many=True)
    class Meta:
        model = DietDay
        fields='__all__'
