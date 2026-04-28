from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    def __str__(self):
        return self.name