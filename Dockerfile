FROM python:3.8

WORKDIR /app
COPY Pipfile* ./

# Only in this case because the app is launched using docker-compose with db
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /app/wait
RUN chmod +x /app/wait

RUN set -ex \
    && pip install -U \
        pip \
        pipenv==2018.11.26 \
    && pipenv install --system --deploy

COPY ./ /app
WORKDIR /app/src

CMD /app/wait && uvicorn main:app --host 0.0.0.0 --port 8000
