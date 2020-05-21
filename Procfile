release: make migrate
web: gunicorn --config gunicorn.conf.py project.wsgi:application
worker: make beat