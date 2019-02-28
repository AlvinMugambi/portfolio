import datetime
from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    The blog model that inherits from the django models model class
    """
    title = models.CharField(max_length=100)
    publish_date = models.DateField(default=datetime.datetime.today)
    image = models.ImageField(upload_to="images/")
    details = models.TextField()
