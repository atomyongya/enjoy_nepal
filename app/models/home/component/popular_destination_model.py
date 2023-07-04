from django.db import models

class PopularDestinationModel(models.Model):
    title = models.CharField(max_length=40)
    image_path = models.ImageField(upload_to='images/home/popular_destination/')

    def __str__(self)-> str:
        return self.title