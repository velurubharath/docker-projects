#Stage1 - build
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Stage 2 - runtime
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /app /app
COPY . . 
CMD ["python", "app.py"]
