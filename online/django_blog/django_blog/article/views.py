from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

def index(request, tags, article_id):
    return HttpResponse(f'Статья {article_id} с тегом {tags}')