from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Objective(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    status = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.status}'

    def get_absolute_url(self):
        return f'{self.pk}'
