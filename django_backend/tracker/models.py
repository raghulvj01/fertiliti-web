from django.db import models
from django.contrib.auth.models import User


class CycleEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.user.username} cycle {self.start_date}"


class MedicineReminder(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='daily')
    time = models.TimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=300, blank=True)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.title} on {self.date}"


class DietPlan(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=50, choices=MEAL_CHOICES)
    food_item = models.CharField(max_length=200)
    calories = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()

    class Meta:
        ordering = ['meal_type']

    def __str__(self):
        return f"{self.meal_type}: {self.food_item}"


class LifestyleLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    sleep_hours = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    exercise_minutes = models.PositiveIntegerField(null=True, blank=True)
    water_glasses = models.PositiveIntegerField(null=True, blank=True)
    stress_level = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']
        unique_together = ['user', 'date']

    def __str__(self):
        return f"{self.user.username} lifestyle {self.date}"
