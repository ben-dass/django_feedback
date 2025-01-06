from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="reviews"),
    path("thank-you/", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews", views.ReviewsListView.as_view(), name="review-list"),
    path("reviews/favorite", views.AddFavoriteView.as_view(), name="add-favorite"),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="review-detail"),
]
