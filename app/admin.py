from django.contrib import admin
from .models.home.home_model import HomeModel
from .models.home.component.kathmandu_tour_model import KathmanduTourModel
from .models.home.component.popular_destination_model import PopularDestinationModel

admin.site.register([
    HomeModel,
    PopularDestinationModel,
    KathmanduTourModel,
])