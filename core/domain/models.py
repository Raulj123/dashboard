import uuid
from django.db import models

class User(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.username

class Income(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, null=True) 
    
    def __str__(self):
        return f"Income: {self.amount}: {self.description}"

class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, null=True) 

    def __str__(self):
        return f"Expense: {self.amount}: {self.description}"

class Payment(models.Model):
    payer_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment Amount: {self.amount}: {self.date}"


