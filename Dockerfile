FROM python:3-alpine

RUN apk add py3-paramiko
WORKDIR /usr/src/app
COPY . .

ENTRYPOINT ["python"]