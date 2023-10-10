from django.contrib import admin
from domain.models import UserProfile, UserPayments, UserExpense


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "occupation",
        "bio"
    )

    search_fields = (
        "user",
    )


class UserPaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "amount",
        "description",
    )

    search_fields = (
        "user",
        "description",
        "amount",
    )


class UserExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "paid",
        "amount",
        "description",
        "payment_interval",
    )

    search_fields = (
        "user",
        "amount",
        "description",
        "payment_interval"
    )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserPayments, UserPaymentAdmin)
admin.site.register(UserExpense, UserExpenseAdmin)

