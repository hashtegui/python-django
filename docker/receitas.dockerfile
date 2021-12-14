FROM python:3.10
MAINTAINER Guilherme Castro
WORKDIR /var/www
COPY . /var/www
COPY /docker/requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "manage.py", "runserver"]
EXPOSE 8000
EXPOSE 5432