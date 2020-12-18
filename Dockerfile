FROM dvcorg/cml-py3:latest

WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app/
CMD sh train.sh
