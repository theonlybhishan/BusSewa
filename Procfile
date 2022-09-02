web: gunicorn core.wsgi
release: python manage.py makemigrations accounts--noinput
release: python manage.py makemigrations bus--noinput
release: python manage.py makemigrations bookings--noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
