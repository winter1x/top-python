"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_blog import views
from django_blog.views import IndexView
#from django.views.generic import TemplateView
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'world'
        return context

urlpatterns = [
    path('', HomePageView.as_view()),
    path('admin/', admin.site.urls),
    path('about/', views.about), # статический маршрут
    path('articles/', include('django_blog.article.urls')),
    #path("users/<int:user_id>/", views.user_profile), # динамический маршрут
    #path("users/<int:user_id>/pets/<int:pet_id>/med_info/", views.med_info_view),
    # глубокий динамический маршрут  /users/42/pets/101/med_info/
    path('users/', include('django_blog.users.urls')),
]
