from app.models.review.review_model import ReviewModel


class ReviewService:
    def getData(
        self,
        review_object: ReviewModel,
    ):
        title = review_object.title
        image = review_object.image

        data = {
            'title': title,
            'image': image,
        }

        return data