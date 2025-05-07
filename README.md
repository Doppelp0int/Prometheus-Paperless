# Prometheus-Paperless
using Papperless-ngx API calls to transfer information to prometheus using a python script inside a docker container

# How to start?
make a new dir in you Linux maschine, paste the Dockerfile and exporter.py into the directory. Run the following commands:

## DockerFile:
```
FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask requests
COPY exporter.py .
EXPOSE 9000
CMD ["python", "exporter.py"]
```

## Build
```
docker build -t paperless-exporter .
```

## Start Container
```
docker run -d -p 9000:9000 --name paperless-exporter paperless-exporter
```
## Check /metrics
open your URL:9000/metrics you should see some information.

# Why?
because we can.
Using a API call from Paperless-ngx, to transfer the information into  Prometheus, so you can import you Paperless Information into Grafana Dashboard.
