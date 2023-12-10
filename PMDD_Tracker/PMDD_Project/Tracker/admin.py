from django.contrib import admin
from Tracker.models import Tracker, User


class TrackerAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Tracker, TrackerAdmin)

# Register your models here.


