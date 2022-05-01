FROM python:3.7

RUN mkdir -p /home

COPY . /home

WORKDIR /home

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5002



