FROM python:3.8.7-slim

WORKDIR /app

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt --no-cache-dir


COPY . ./


# Entrypoint for the image
CMD ["python3", "./status_loop.py"]