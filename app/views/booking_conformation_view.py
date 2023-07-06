from rest_framework.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser

from app.services.booking.booking_service import BookingService

class BookingConformationView(View):
    def get(self, request):

        user = request.user

        data = {
            'user': user,
        }

        return render(
            request,
            'booking/component/booking_conformation.html',
            data,
        )