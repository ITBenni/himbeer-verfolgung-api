FROM python:3.12-slim-bookworm

RUN mkdir -p /srv
WORKDIR /srv

COPY requirements.txt /srv/

RUN pip3 install --no-cache-dir -r requirements.txt --upgrade

COPY . /srv

WORKDIR /srv/api
EXPOSE 8000

ENTRYPOINT [ "gunicorn" ]
CMD ["-w", "4" ,"-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "app:app"]
