FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=engine_app.app:create_app
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
