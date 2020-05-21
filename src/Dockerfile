FROM python:3.7-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w 2", "-b", "0.0.0.0:8000" , "app:app"]