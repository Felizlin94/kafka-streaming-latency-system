FROM python:3.10

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app

CMD ["python", "-m", "app.producer.producer"]