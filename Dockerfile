FROM python:3-alpine

RUN apk add --virtual .paramiko_dependencies \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    build-base \
    py-pip \
&&  apk add zlib \
    zlib-dev \
    libssl1.1 \
&&  pip install cffi \
&&  pip install paramiko \
&&  apk del .paramiko_dependencies

CMD ["python"]
