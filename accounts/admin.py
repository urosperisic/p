# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sessions.models import Session

from .models import CustomUser


class SessionAdmin(admin.ModelAdmin):
    list_display = ("session_key", "_session_data", "expire_date")
    readonly_fields = ("_session_data",)

    def _session_data(self, obj):
        return obj.get_decoded()


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Session, SessionAdmin)
