from django.contrib import admin
from .models import Tracker



class TrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'date', 'periodflow', 'irritation', 'sadness', 'happiness', 'loneliness')  # 'name' used in list
    pass

class UserAdmin(admin.ModelAdmin):
    pass

# admin.site.register(User, UserAdmin)
admin.site.register(Tracker, TrackerAdmin)

# Register your models here.


