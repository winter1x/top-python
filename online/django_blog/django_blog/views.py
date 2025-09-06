from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
        request,
        'index.html',
        context={'who': 'world'},
    )

def index(request):
    return render(
        request,
        'index.html',
        context={'who': 'world'},
    )

def about(request):
    tags = ['программировние', 'tag2', 'tag3']
    return render(
        request, 
        'about.html', 
        context={'tags': tags})

# def med_info_view(request, user_id, pet_id):
#     ...