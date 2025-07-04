FROM python:3.10-slim
LABEL authors='Jakub Kondek, SDA'

ENV HOSTNAME=0.0.0.0
ENV PORT=8000

MAINTAINER Jakub

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV HOSTNAME=0.0.0.0
ENV PORT=8000
CMD ["sh", "-c", "uvicorn app:app --host ${HOSTNAME} --port ${PORT}"]
