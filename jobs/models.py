from django.db import models

# Create your models here.
class Job(models.Model):
    """
    The job object that inherits from the django models model class
    """
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
