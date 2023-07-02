from django.db import models

class HomeModel(models.Model):
    home_main_image = models.ImageField()