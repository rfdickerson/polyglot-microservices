FROM python:2-alpine

COPY requirements.txt /tmp/requirements.txt
RUN cd /tmp && pip install -r requirements.txt

WORKDIR /usr/app

