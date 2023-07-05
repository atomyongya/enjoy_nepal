from rest_framework.views import View
from django.shortcuts import render

from app.models.review.review_model import ReviewModel
from app.services.review.review_service import ReviewService

class ReviewView(View):
    def get(self, request):
        review_object = ReviewModel.objects.first()
        review_service = ReviewService()

        data = review_service.getData(
            review_object=review_object,
        )

        return render(
            request,
            'review/review.html',
            data,
        )