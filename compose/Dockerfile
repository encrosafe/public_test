FROM python:3.9-alpine3.13
LABEL maintainer="londonappdeveloper.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements/requirements.txt /requirements/requirements.txt
COPY ./public_test /public_test

WORKDIR /public_test
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home public_test && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R public_test:public_test /vol && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER public_test


