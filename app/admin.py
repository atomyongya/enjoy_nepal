from django.contrib import admin
from .models.home.home_model import HomeModel
from .models.home.component.kathmandu_tour_model import KathmanduTourModel
from .models.home.component.popular_destination_model import PopularDestinationModel
from .models.detail.detail_model import DetailModel
from .models.detail.component.customer_service_model import CustomerServiceModel
from .models.detail.component.detail_info_model import DetailInfoModel
from .models.detail.component.itinary_model import ItinaryModel

admin.site.register([
    HomeModel,
    PopularDestinationModel,
    KathmanduTourModel,
    DetailModel,
    CustomerServiceModel,
    DetailInfoModel,
    ItinaryModel,
])