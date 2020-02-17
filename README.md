# Taxi-app
Здесь реализованы первые две части тестового задания.

БД - PostgreSQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'taxiapp',
         'USER' : 'admin',
         'PASSWORD' : 'v320',
         'HOST' : 'localhost',
         'PORT' : '5432',
    }
}


Для загрузки в базу данных машин просьба запустить сид командой python manage.py loaddata сars.json

Для логина необходимо создать суперюзера
