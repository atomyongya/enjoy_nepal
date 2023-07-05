from django.urls import path
from app.views.hotel_detail_view import HotelDetailView

from app.views.hotel_view import HotelView
from .views.home_view import HomeView
from .views.detail_view import DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail-layout', DetailView.as_view(), name='detail_layout'),
    path('hotel', HotelView.as_view(), name='hotel'),
    path('hotel_detail', HotelDetailView.as_view(), name='hotel_detail'),
]