from django.db import models

# Create your models here.
from django.db import models

class Document(models.Model):

    uploadedFile = models.ImageField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)