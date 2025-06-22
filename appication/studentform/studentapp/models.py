from django.db import models

# Create your models here.
class StudentApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name