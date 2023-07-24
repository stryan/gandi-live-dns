FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/gandi-live-dns.py .
COPY src/config.py .

CMD ["python3", "gandi-live-dns.py"]
