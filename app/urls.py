from django.urls import path
from app.views.hotel_detail_view import HotelDetailView

from app.views.hotel_view import HotelView
from app.views.review_view import ReviewView
from app.views.things_to_do_detail_view import ThingsToDoDetailView
from app.views.things_to_do_view import ThingsToDoView
from app.views.vacation_rentals_detail_view import VacationRentalsDetailView
from app.views.vacation_rentals_view import VacationRentalsView
from .views.home_view import HomeView
from .views.detail_view import DetailView
from authentication.views.sign_in_view import logout

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail-layout', DetailView.as_view(), name='detail_layout'),
    path('hotel', HotelView.as_view(), name='hotel'),
    path('hotel_detail', HotelDetailView.as_view(), name='hotel_detail'),
    path('things-to-do', ThingsToDoView.as_view(), name='things_to_do'),
    path('things-to-do-detail', ThingsToDoDetailView.as_view(), name='things_to_do_detail'),
    path('vacation-rentals', VacationRentalsView.as_view(), name='vacation_rentals'),
    path('vacation-rentals-detail', VacationRentalsDetailView.as_view(), name='vacation_rentals_detail'),
    path('review', ReviewView.as_view(), name='review'),
    path('logout', logout, name='logout'),
]