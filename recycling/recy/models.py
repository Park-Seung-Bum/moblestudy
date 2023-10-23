from django.db import models

# Create your models here.
from django.db import models

class Image(models.Model):
    image_name = models.CharField(max_length=255)
    image_data = models.BinaryField()
    upload_date = models.DateTimeField(auto_now_add=True)