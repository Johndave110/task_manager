from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(default=now)
    
    def status(self):
        today = now().date()
        if self.due_date == today:
            return 'Due Today'
        elif self.due_date > today:
            return 'Upcoming'
        else:
            return 'Overdue'
    
    def __str__(self):
        return self.title