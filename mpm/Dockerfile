
FROM python:3.9-slim


WORKDIR /mpm-teenyfi-backend


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*


COPY mpm/requirements.txt .


RUN pip install  -r requirements.txt


COPY . .

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
