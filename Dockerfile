FROM python:3.9.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    # needed on Alpine for the cryptography and psycopg2 packages
    && apk add gcc postgresql-dev musl-dev python3-dev libffi-dev openssl-dev cargo

RUN addgroup -S django
RUN adduser \
    --disabled-password \
    --ingroup django \
    django

USER django:django

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
COPY --chown=django:django Pipfile Pipfile.lock .
RUN python -m pipenv install --dev --system --deploy --ignore-pipfile

EXPOSE 8888

COPY --chown=django:django . .
