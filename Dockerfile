FROM python:3.8.6-slim-buster as build

RUN apt-get update && apt-get install -y build-essential

RUN groupadd -g 999 trainer && \
    useradd -r -m -u 999 -g trainer trainer
WORKDIR /home/trainer/app
RUN chown -R trainer:trainer /home/trainer/

RUN pip install pipenv

USER trainer

COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy

COPY train.py ./

ENTRYPOINT ["pipenv", "run"]
CMD ["python", "train.py"]
