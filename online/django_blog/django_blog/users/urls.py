from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_view, name='index'),
    #path('<int:user_id>/pets/<int:pet_id>/med_info/', views.pet_med_info_view),
    path(
        '<int:user_id>/pets/<int:pet_id>/med_info/',
        views.pet_med_info_view,
        name='pet_med_info',
    ),
    path('update/<int:pk>', views.UserUpdateView.as_view(), name='update'),
]