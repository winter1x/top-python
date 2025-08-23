"""
uv init django_blog
cd django_blog
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv add django
uv run django-admin startproject django_blog .
uv run django-admin version
uv run manage.py runserver
uv run manage.py migrate
django-admin startapp article

runserver - запуск сервера ращработки
migrate - применение миграций
makemigrations - создание миграций 
shell - работа с базой через интерактивную оболочку
createsuperuser - создание суперпользователя для админки
test - запуск тестов
startapp - генерация приложений


{% if user.is_authenticated %}
    <p>Привет, {{ user.username }}!</p>
{% else %}
    <p>Пожалуйста, <a href="{% url 'login' %}">войдите</a> или <a href="{% url 'register' %}">зарегистрируйтесь</a>.</p>
{% endif %}

<ul>
    {% for article in articles %}
        <li><a href="{% url 'article_detail' article.id %}">{{ article.title }}</a></li>
    {% endfor %}
</ul>

django.template.context_processors.request - добавляет переменную request в контекст шаблона
django.template.context_processors.debug - добавляет переменную DEBUG в контекст шаблона

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Проверка логина и пароля
        return HTTPResponse('Логин и пароль введены верно')

from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def login_view(request):
    ...

from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, world!')
        
конвертеры для динамических URL
int - целое число
str - строка без слешей
slug - строка из латинских букв и цифр и дефисов и подчеркиваний
uuid - уникальный идентификатор формата uuid
path - строка может содержать слеши


"""