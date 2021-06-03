from django.contrib import admin
from .models import (
    DietType,
    IngredientPortion,
    CookingStep,
    Meal,
    DietDay,
    Diet, UserDiet, UserDietDay,
)
from django.db.models import Sum


class CookingStepInLine(admin.TabularInline):
    model = CookingStep
    extra = 3


class IngredientPortionInLine(admin.TabularInline):
    model = IngredientPortion
    extra = 3


class MealAdmin(admin.ModelAdmin):
    list_display = ("name", "meal_type", "cooking_time", "kcal")
    inlines = [CookingStepInLine, IngredientPortionInLine]


class UserDietDayAdmin(admin.ModelAdmin):
    list_display = ("diet_day_date",)


class UserDietAdmin(admin.ModelAdmin):
    list_display = ("start_date", "end_date")


class DietDayAdmin(admin.ModelAdmin):
    list_display = ("name", "kcal", "macronutrients")
    readonly_fields = ['kcal', 'macronutrients']

    def save_model(self, request, obj, form, change):
        self.instance = obj
        return super().save_model(request, obj, form, change)

    def save_related(self, request, obj, form, change):
        result = super().save_related(request, obj, form, change)
        meals = self.instance.meals.all()
        calories = meals.aggregate(Sum('kcal'))
        proteins = meals.aggregate(Sum('proteins')).get('proteins__sum')
        fats = meals.aggregate(Sum('fats')).get('fats__sum')
        carbohydrates = meals.aggregate(
            Sum('carbohydrates')).get('carbohydrates__sum')
        if proteins and fats and carbohydrates:
            self.instance.macronutrients = str(
                proteins) + "/" + str(fats) + "/" + str(carbohydrates) + " B/T/W"
        else:
            self.instance.macronutrients = "unknown"
        self.instance.kcal = calories.get('kcal__sum')
        self.instance.save()
        return result


class DietAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_in_days',
                    'average_kcal_per_day', 'diet_type', 'public')
    readonly_fields = ['average_kcal_per_day']

    def save_model(self, request, obj, form, change):
        self.instance = obj
        return super().save_model(request, obj, form, change)

    def save_related(self, request, obj, form, change):
        result = super().save_related(request, obj, form, change)
        dietdays = self.instance.diet_days.all()
        total_calories = dietdays.aggregate(Sum('kcal'))
        average_calories = total_calories.get('kcal__sum') // dietdays.count()
        self.instance.average_kcal_per_day = average_calories
        self.instance.save()
        return result


admin.site.register(DietType)
admin.site.register(Meal, MealAdmin)
admin.site.register(DietDay, DietDayAdmin)
admin.site.register(Diet, DietAdmin)
admin.site.register(UserDietDay, UserDietDayAdmin)
admin.site.register(UserDiet, UserDietAdmin)
