from django.contrib import admin
from core.models import UserAlert
from safedelete.admin import highlight_deleted, SafeDeleteAdmin

# Register your models here.
@admin.register(UserAlert)
class UserAlertAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, 'id', 'price', 'triggered', 'deleted')
