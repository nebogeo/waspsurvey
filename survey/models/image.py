from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to='static/image_uploads')
    
