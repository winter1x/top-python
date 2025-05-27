from django.shortcuts import render

def index(requests):
    return render(
        requests,
        'index.html',
        context={
            'who': 'World',
        },
    )

def about(requests):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        requests,
        'about.html',
        context={'tags': tags},
        )