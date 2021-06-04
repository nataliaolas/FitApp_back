from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

"""
TODO:
    Napisac testy dla modeli.
"""


class DietType(models.Model):
    """ model for diet type e.g. vegan / non vegan / low carbs etc."""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Meal(models.Model):
    """ model that represents recipes"""
    BREAKFAST = '0'
    LUNCH = '1'
    DINNER = '2'
    TEA = '3'
    SUPPER = '4'
    SNACK = '5'
    EAT_WHENEVER_YOU_WANT = '6'

    MEAL_TYPE_CHOICES = [
        (BREAKFAST, _('śniadanie')),
        (LUNCH, 'drugie śniadanie'),
        (DINNER, 'obiad'),
        (TEA, 'podwieczorek'),
        (SUPPER, 'kolacja'),
        (SNACK, 'przekąska'),
        (EAT_WHENEVER_YOU_WANT, 'Dobry na każdą porę dnia')
    ]
    name = models.CharField(max_length=30, default="Przykladowy posilek")
    picture = models.ImageField(
        'Zdjecie posilku', null=True, blank=True, upload_to='diet_planner/meals')
    public = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    meal_type = models.CharField(max_length=1, choices=MEAL_TYPE_CHOICES,
                                 default=EAT_WHENEVER_YOU_WANT, null=True, blank=True)
    cooking_time = models.IntegerField('Czas przyrządzenia w minutach:')
    kcal = models.IntegerField()
    proteins = models.IntegerField(null=True, blank=True)
    fats = models.IntegerField(null=True, blank=True)
    carbohydrates = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.author.is_superuser:
            self.public = True
        else:
            self.public=False
        super(Meal, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    def get_cooking_steps(self):
        return self.cookingstep_set.all()

    def get_ingredients(self):
        return self.ingredientportion_set.all()


class CookingStep(models.Model):
    """ model that contains steps needed to cook meal """
    step = models.TextField()
    meal = models.ForeignKey(Meal, related_name='steps',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.step


class IngredientPortion(models.Model):
    """ model that repesents ingredients in the meal """
    ingredient = models.CharField(max_length=50, default="Przykladowy składnik")
    portion = models.CharField(max_length=30)
    meal = models.ForeignKey(Meal, related_name='ingredients',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ingredient


class Diet(models.Model):
    """ model that represents diets """
    name = models.CharField(max_length=30, default="Przykladowa dieta")
    picture = models.ImageField(
        'Zdjecie diety', null=True, blank=True, upload_to='diet_planner/diets')
    public = models.BooleanField(default=True)
    description = models.TextField()
    duration_in_days = models.IntegerField(default=30)
    average_kcal_per_day = models.IntegerField(null=True, blank=True)
    diet_type = models.ForeignKey(
        DietType, on_delete=models.SET_NULL, null=True)
    diet_days = models.ManyToManyField('DietDay')

    def __str__(self):
        return self.name


class DietDay(models.Model):
    """ model that represents single day in diet """
    name = models.CharField(max_length=20, null=True,
                            blank=True, default=_("My diet day"))
    meals = models.ManyToManyField(Meal)
    kcal = models.IntegerField(null=True, blank=True)
    macronutrients = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name + " " + str(self.kcal) + " " + self.macronutrients


class UserDiet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    start_date = models.DateField(_('diet start date'), null=True, blank=True)
    end_date = models.DateField(_('diet end date'), null=True, blank=True)

    def __str__(self):
        return self.diet.name + " " + str(self.start_date) + " " + str(self.end_date)


class UserDietDay(models.Model):
    diet = models.ForeignKey(UserDiet, on_delete=models.CASCADE)
    diet_day = models.ForeignKey(DietDay, on_delete=models.CASCADE)
    diet_day_date = models.DateField(_('diet day date'), null=True, blank=True)

    def __str__(self):
        return self.diet.diet.name + " " + self.diet_day.name + " " + str(self.diet_day_date)


class FavouriteMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'meal:{self.meal}, user:{self.user}'


class FavouriteDiet(models.Model):
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'meal:{self.meal}, user:{self.user}'

class UserMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'meal:{self.meal}, user:{self.user}'