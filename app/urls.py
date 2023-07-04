from django.urls import path
from .views.home_view import HomeView
from .views.detail_view import DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail-layout', DetailView.as_view(), name='detail_layout'),
]