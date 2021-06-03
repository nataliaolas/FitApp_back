from django.db import models
from django.contrib.auth.models import User


"""
TODO:
    ??
"""


class Profile(models.Model):
    avatar = models.ImageField(
        'Zdjecie profilowe', null=True, blank=True, upload_to='UserProfile/')
    height = models.FloatField('Wzrost użytkownika', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Measurement(models.Model):
    bmi = models.FloatField(null=True, blank=True)
    weight = models.FloatField()
    caloric_demand = models.IntegerField(null=True, blank=True)
    chest_circumference = models.FloatField(null=True, blank=True)
    hip_circumference = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    biceps_circumference = models.FloatField(null=True, blank=True)
    date_of_measurement = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " weight " + str(self.weight) + "kg" + " date of measurement " + str(self.date_of_measurement)
