from django.db import models

# Create your models here.


class Todo(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    due_date=models.DateField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)