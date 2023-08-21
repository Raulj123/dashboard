from django.contrib import admin
from domain.models import User, Income, Expense, Payment

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "created",
        "updated",
        "occupation",
        "bio"
    )

    search_fields = (
        "username",
    )

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "payer_user_id",
        "date",
    )

    search_fields = (
        "payer_user_id",
        "amount",
    )

class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "amount",
        "description",
    )

    search_fields = (
        "user_id",
    )

class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "amount",
        "description",
    )

    search_fields = (
        "user_id",
    )




admin.site.register(User, UserAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Payment, PaymentAdmin)