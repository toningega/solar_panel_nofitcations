FROM python:3.8.7-slim

WORKDIR /app

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt --no-cache-dir


COPY . ./

# Run service
# CMD [ "uvicorn", "--port=3000", "ApiClient:app", "--host=0.0.0.0"]

# Entrypoint for the image
CMD ["python3", "./my_battery.py"]