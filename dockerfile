FROM python:3.7

RUN mkdir -p /home

COPY . /home

RUN pip install -r requirements.txt

