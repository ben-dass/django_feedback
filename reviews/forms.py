from django import forms

from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="User",
#         max_length=100,
#         error_messages={
#             "required": "User must not be empty",
#             "max_length": "Please enter a shorter name",
#         },
#     )
#
#     review_text = forms.CharField(
#         label="Feedback",
#         widget=forms.Textarea,
#         max_length=200,
#     )
#
#     rating = forms.IntegerField(
#         label="Rating",
#         min_value=1,
#         max_value=5,
#     )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = "__all__"

        labels = {
            "user_name": "User",
            "review_text": "Review",
            "rating": "Rating",
        }

        error_messages = {
            "user_name": {
                "required": "User must not be empty",
                "max_length": "Please enter a shorter name",
            }
        }
