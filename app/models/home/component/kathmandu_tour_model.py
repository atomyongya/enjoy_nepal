from django.db import models

class KathmanduTourModel(models.Model):
    title = models.CharField(max_length=40)
    image_path = models.ImageField(upload_to='images/home/kathmandu_tour/')

    def __str__(self) -> str:
        return self.title