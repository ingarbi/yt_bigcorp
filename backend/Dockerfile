FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev
RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev
RUN apt-get install -y gobject-introspection
RUN apt-get update && apt-get install -y libpango-1.0-0 libpangoft2-1.0-0

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip --no-warn-script-location

RUN pip install -r requirements.txt --no-cache-dir --no-warn-script-location

COPY . .