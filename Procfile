web: gunicorn app.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python app/manage.py collectstatic --noinput
release: python app/manage.py migrate