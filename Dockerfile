FROM python:3-alpine

RUN apk add py3-paramiko

CMD ["python"]