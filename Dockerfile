FROM python:3

RUN pip install --no-cache-dir paramiko

CMD ["python"]