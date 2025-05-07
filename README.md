# Prometheus-Paperless
using Paperless-ngx API calls to transfer information to prometheus using a python script inside a docker container

# How to start?
make a new dir in your linux machine, paste the Dockerfile and exporter.py into the directory. Run the following commands:

## Build
```
docker build -t paperless-exporter .
```

## Start Container
```
docker run -d -p 9000:9000 --name paperless-exporter paperless-exporter
```
## Check /metrics
open your URL:9000/metrics you should see some information, like paperless_documents_total


# How to implement into prometheus?
paste this block into your prometheus.yml
```
scrape_configs:
  - job_name: 'paperless_exporter'
    static_configs:
      - targets: ['localhost:9000']
```


# Why?
because we can.
Using a API call from Paperless-ngx, to transfer the information into Prometheus, so you can import you Paperless Information into Grafana Dashboard.
