#Stage 1 as Builder
FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --user -r requirements.txt

#Stage 2

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

COPY app.py /app/app.py

COPY requirements.txt /app/requirements.txt

CMD ["python","app.py"] 

