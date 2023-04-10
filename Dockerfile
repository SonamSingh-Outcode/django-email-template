FROM python:3.10-alpine

ENV PYTHONBUFFERED 1

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    ca-certificates gcc linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev libc-dev \
    postgresql-dev

WORKDIR /email-boilerplate

ADD requirements.txt /email-boilerplate/

RUN pip install -r /email-boilerplate/requirements.txt

COPY ./ /email-boilerplate