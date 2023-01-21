FROM python:3.9-slim

COPY requirements.txt ./requirements.txt

RUN apt-get update
RUN apt-get -y install python3-tk

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8080

CMD python index.py