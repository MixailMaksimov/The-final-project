from django.db import models


# Create your models here.
class RepairRequest(models.Model):

    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершен'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Высокий'),
        (2, 'Средний'),
        (3, 'Низкий'),
    ]

    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    description = models.TextField()
    student_name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



