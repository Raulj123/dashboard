from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    occupation = models.CharField(max_length=200, default='unkown')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserPayments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"Payment by {self.user} on {self.description}"


class UserExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    paid = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2, max_digits=11, null=True)
    description = models.TextField(max_length=300)
    payment_interval = models.TextField(max_length=30)
