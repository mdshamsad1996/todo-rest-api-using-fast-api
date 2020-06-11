FROM python:3.7

MAINTAINER shamsad alam "alam.shams.1996@gmail.com"

WORKDIR /app
COPY src/ /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD uvicorn myapp:app --host 0.0.0.0 --port 8000 --reload