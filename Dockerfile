FROM python:3.8.7-slim-buster
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y gettext libgettextpo-dev
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY ./charts/. /code/