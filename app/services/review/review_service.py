from app.models.review.review_model import ReviewModel


class ReviewService:
    def getData(
        self,
        review_object: ReviewModel,
    ):
        title = review_object.title
        image = review_object.image
        review = review_object.website_review_detail

        data = {
            'title': title,
            'image': image,
            'review': review,
        }

        return data