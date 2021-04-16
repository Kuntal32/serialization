from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    class Meta:
        db_table = 'teaher'
