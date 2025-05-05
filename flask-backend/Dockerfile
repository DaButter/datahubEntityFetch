# flask-backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app
ENV PYTHONPATH=/app
ENV FLASK_APP=api.py
ENV FLASK_ENV=production

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers=4", "--timeout=120", "api:app"]