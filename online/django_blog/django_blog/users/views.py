from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import User

def users_view(request):
    users = User.objects.all()
    return render(request, 'users_list.html', context={'users': users})
    
def pet_med_info_view(request, user_id, pet_id):
    return render(
        request,
        'med_info.html',
        context={'user_id': user_id, 'pet_id': pet_id, 'type': f'{reverse("pet_med_info", kwargs={"user_id": user_id, "pet_id": pet_id})}'},
    )
