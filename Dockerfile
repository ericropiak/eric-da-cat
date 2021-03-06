# Dockerfile is used for product deployments (not actually used by OpenShift :( )
FROM python:3.7-alpine

COPY requirements.txt requirements.txt
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt


COPY . /app
WORKDIR /app

ENV FLASK_ENV=prod

EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "--log-level", "INFO", "manage:app" ]