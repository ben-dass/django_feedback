from django.views.generic import CreateView, ListView

from profiles.models import UserProfile


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles/"


class ProfilesView(ListView):
    template_name = "profiles/user_profiles.html"
    model = UserProfile
    context_object_name = "profiles"
