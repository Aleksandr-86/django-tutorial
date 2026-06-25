## Создание проекта с нуля
- Python 3.14.6
- Poetry 2.4.1
- Django 6.0.6
### Создание шаблона нового Python проекта
```sh
poetry new django-tutorial
```
### Добавление пакета-зависимости  
[Корневая папка проекта](./)
```sh
poetry add django
```
После выполнения команды также будет настроено виртуальное окружение. При этом файлы виртуального окружения будут размещены в корне проекта в папке .venv при соответствующей конфигурации poetry.  

### Активация виртуального окружения
```sh
eval $(poetry env activate)
```
Также можно обойтись и без активации если использовать команду `poetry run`
### Создание Django проекта
[src/django_tutorial](src/django_tutorial)
```sh
poetry run django-admin startproject my_site .
```
(точка в конце последней команды не будет создавать корневую папку, разместив файлы в существующей папке django_tutorial)
### Запуск сервера для разработки
[src/django_tutorial](src/django_tutorial)
```sh
poetry run python manage.py runserver
```
### Создание приложения "polls"
[src/django_tutorial](src/django_tutorial)
```sh
poetry run python manage.py startapp polls
```
