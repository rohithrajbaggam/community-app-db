from django.urls import path, include 


urlpatterns = [
    path("api/website/", include("userprofile.website.urls")),
]

