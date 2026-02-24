FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir uv

COPY uv.toml requirements.txt ./
RUN uv pip install --system -r requirements.txt

COPY . .

CMD ["celery", "-A", "worker.main.celery_app", "worker", "--loglevel=info"]
