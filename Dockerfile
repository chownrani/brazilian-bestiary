FROM python:3.13-alpine AS builder

WORKDIR /app

RUN apk add --no-cache build-base

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
