from django.contrib import admin

from app.models.hotel.component.hotel_detail_model import HotelDetailModel
from .models.home.home_model import HomeModel
from .models.home.component.kathmandu_tour_model import KathmanduTourModel
from .models.home.component.popular_destination_model import PopularDestinationModel
from .models.detail.detail_model import DetailModel
from .models.detail.component.customer_service_model import CustomerServiceModel
from .models.detail.component.detail_info_model import DetailInfoModel
from .models.detail.component.itinary_model import ItinaryModel
from .models.hotel.hotel_model import HotelModel
from .models.hotel.component.hotel_service_model import HotelServiceModel
from .models.user_reviews.user_review_model import UserReviewModel

admin.site.register([
    HomeModel,
    PopularDestinationModel,
    KathmanduTourModel,
    DetailModel,
    CustomerServiceModel,
    DetailInfoModel,
    ItinaryModel,
    HotelModel,
    HotelServiceModel,
    UserReviewModel,
    HotelDetailModel,
])