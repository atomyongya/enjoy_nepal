from django.shortcuts import render
from rest_framework.views import View

class HomeView(View):
    def get(self, request):
        return render(
            request,
            'home/home.html'
        )