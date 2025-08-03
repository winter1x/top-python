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
"""