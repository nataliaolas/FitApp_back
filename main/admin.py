from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Measurement, Profile
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class MeasurementAdmin(admin.ModelAdmin):
    model = Measurement
    list_display = ("user", "date_of_measurement")

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'get_height')

    def get_height(self, instance):
        return instance.profile.height
    get_height.short_description = 'height'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Measurement, MeasurementAdmin)
