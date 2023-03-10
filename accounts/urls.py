from django.urls import path, include 
urlpatterns = [
    path("api/websites/", include("accounts.website.urls")),
]
