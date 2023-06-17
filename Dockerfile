FROM python:3.10.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /code/
RUN python manage.py collectstatic

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "iPortfolio_projet.wsgi:application"]