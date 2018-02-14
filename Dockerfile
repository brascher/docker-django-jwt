FROM python:3

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y netcat-openbsd
RUN apt-get install -y libmysqlclient-dev

COPY ./docker-entrypoint.sh .
COPY ./mycatalog ./
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8005" ]