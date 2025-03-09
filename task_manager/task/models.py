from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ("Overdue", "Overdue"),
        ("Due Today", "Due Today"),
        ("Upcoming", "Upcoming"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, editable=False)

    def save(self, *args, **kwargs):
        # Automatically set status before saving
        today = date.today()
        if self.due_date < today:
            self.status = "Overdue"
        elif self.due_date == today:
            self.status = "Due Today"
        else:
            self.status = "Upcoming"
        super().save(*args, **kwargs)