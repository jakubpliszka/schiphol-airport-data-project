FROM python:3.9-slim

COPY . .

RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000

RUN useradd -ms /bin/bash django-user
USER django-user
