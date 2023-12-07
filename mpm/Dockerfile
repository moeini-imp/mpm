# Use an official Python runtime as a parent image
FROM python:3.11-alpine
WORKDIR /mpm-teenyfi-backend
COPY . /mpm-teenyfi-backend
RUN apk add --no-cache build-base libffi-dev openssl-dev
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV NAME World
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
