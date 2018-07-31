FROM python:alpine3.7

RUN apk update && apk add --no-cache git openssh-client

RUN addgroup -S -g 1001 app \
    && adduser -S -D -h /app -u 1001 -G app app

ENV PYTHONUNBUFFERED 1
ENV LOG_LEVEL DEBUG

RUN mkdir -p /app/csv_files
WORKDIR /app

RUN pip install -U pip pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN set -ex && pipenv install --dev --deploy --system

COPY . /app
RUN chown -R app.app /app/
RUN chmod +x /app/sort_csv.py

USER app

ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]
