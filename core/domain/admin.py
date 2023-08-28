from django.contrib import admin
from domain.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "occupation",
        "bio"
    )

    search_fields = (
        "username",
    )


admin.site.register(UserProfile, UserProfileAdmin)

