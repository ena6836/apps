from django.db import models
from PIL import Image

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
