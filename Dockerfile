FROM python:3.8.6-slim-buster as build

RUN apt-get update && apt-get install -y build-essential git

WORKDIR /app

RUN pip install pipenv dvc[gs]

COPY Pipfile ./
RUN pipenv install --skip-lock

COPY . ./

CMD ["sh", "train.sh"]
