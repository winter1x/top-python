from django.shortcuts import render

def index(request):
    return render(
        request,
        'index.html',
        context={'who': 'world'},
    )

def about(request):
    tags = ['tag1', 'tag2', 'tag3']
    return render(
        request, 
        'about.html', 
        context={'tags': tags})