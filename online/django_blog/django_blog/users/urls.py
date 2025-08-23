from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_view),
    path('<int:user_id>/pets/<int:pet_id>/med_info/', views.pet_med_info_view),
]