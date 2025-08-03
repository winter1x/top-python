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
"""