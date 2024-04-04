FROM python:latest

COPY dvk.py /app/dvk.py

WORKDIR /app

CMD ["python", "dvk.py"]
