web: gunicorn django_project.wsgi:application --log-file - --log-level debug
web: python manage.py collectstatic --noinput
web: manage.py migrate