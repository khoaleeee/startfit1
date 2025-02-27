from django.contrib import admin

from .models import TrackedActivitie
# User, Activitie,

# Register your models here.
# admin.site.register(User)
# admin.site.register(Activitie)

class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('activityType',)

admin.site.register(TrackedActivitie, ActivityAdmin)