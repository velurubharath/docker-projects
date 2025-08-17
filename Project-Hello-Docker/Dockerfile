FROM python:3.9-alpine

WORKDIR /app

COPY app/ app/

RUN pip install flask

EXPOSE 5000

CMD ["python","app/app.py"]




