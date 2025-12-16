from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser, JobApplication, InteractionNote

# Register your models here.
class CustomAdminUser(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")

admin.site.register(CustomUser, CustomAdminUser)

# Register your models here.
admin.site.register(JobApplication)
admin.site.register(InteractionNote)
