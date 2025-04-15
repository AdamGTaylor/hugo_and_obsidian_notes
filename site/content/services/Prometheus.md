---
title: "Prometheus"
date: 2025-04-02
draft: false
tags: ["alerting", "monitoring", "guide"]
categories: ["service"]
---
## Description
Prometheus is a free software application for monitoring and alerting. It records and pulls data from defined sources and stores it in its time series database which uses postgreSQL.

## How to Set it up
As usual, I went with the official docker image.

### Docker-compose file

``` yaml
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    restart: unless-stopped
    volumes:
      - ../prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--web.enable-lifecycle'
    ports:
      - 9091:9090
    deploy:
      resources:
        limits:
          cpus: "1"
          memory: "2G"
        reservations:
          cpus: "0.1"
          memory: "1G"
```
This will be our first time seeing a different port mapped to the host and the docker container. The reason is that one of my services is already using 9090, which I did not intend to change. This won't cause any issues anywhere, we just have to be consistent with setting NPM proxy hosts.

### Config file
Prometheus needs a config (prometheus.yml) file that defines how to handle things and what information needs to be collected. If everything is okey, the panel will tell you so. My config file is very simple:
``` yaml
lobal:
  scrape_interval: 15s
  scrape_timeout: 10s

#alerting:
#  alertmanagers:
#  - static_configs:
#    - targets: []
#    scheme: http
#    timeout: 10s
#    api_version: v1

scrape_configs:
  - job_name: 'prometheus'
    honor_timestamps: true
    scrape_interval: 15s
    scrape_timeout: 10s
    metrics_path: /metrics
    scheme: http
    static_configs:
      - targets:
        - 192.168.1.11:9091

  - job_name: 'aversion1-node'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['192.168.1.11:8081']
```
You can notice two things:
- "job_name: prometheus": this is were we post our collected information.
- "job_name": generally consist of different jobs where we define targets. As you can notice, the target can be an ip:port or a docker container name. (This is similar to NPM.)
The above jobs will gather information from node-exporter (host monitoring) and cadvisor(docker container monitoring).
## Extra 

### Visualisation
Means of visualisation can be done by something custom, but it very handy to use [[Grafana]] for this.

## Sources

Coming soon.