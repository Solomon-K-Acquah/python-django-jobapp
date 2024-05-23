from django.db import models

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
# file upload model/table
class UploadFile(models.Model):
    file = models.FileField(upload_to='files')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
    
