from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    members = models.ManyToManyField(User, related_name='tasks', blank=True)
    STATUS_CHOICES = (
        ('Todo', 'Todo'),
        ('Inprogress', 'Inprogress'),
        ('Done', 'Done'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Todo')

    def __str__(self):
        return self.task_name