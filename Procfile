release: python3 src/manage.py migrate
heroku ps:scale web=1
web: gunicorn src/api.wsgi