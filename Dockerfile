FROM python:3.14
WORKDIR /api
COPY . /api

RUN pip install fastapi[standard]
