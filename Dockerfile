FROM python:3.9

ADD dvk.py /app/dvk.py

ADD dvk.txt /app/dvk.txt

RUN cat /app/dvk.txt

CMD ["python", "/app/dvk.py"]