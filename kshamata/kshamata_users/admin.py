from django.contrib import admin
from models import Women, Volunteer, Activity
# Register your models here.


class WomenAdmin(admin.ModelAdmin):
    list_display = ('aadhar_id', 'name', 'dob', 'contact', 'cur_salary', 'cur_location')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'location',  'response_shelter', 'respone_women', 'women')


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'Women')


admin.site.register(Women, WomenAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Activity, ActivityAdmin)

