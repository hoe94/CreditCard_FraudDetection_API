FROM python:3.7

RUN mkdir -p /home

COPY . /home

WORKDIR /home

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5002

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:5002", "src.app:app" ]

