web: gunicorn app.wsgi --log-file -
heroku ps:scale web=1
python app/manage.py collectstatic --noinput
release: python app/manage.py migrate