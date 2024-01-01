from django.contrib import admin
from core.models import UserAlert

# Register your models here.
class UserAlertAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'triggered']

admin.site.register(UserAlert, UserAlertAdmin)
