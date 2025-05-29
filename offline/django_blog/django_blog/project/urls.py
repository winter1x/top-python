from django.urls import path, include
from project.users import views

urlpatterns = [
    path("users/", include("project.users.urls")),
]
