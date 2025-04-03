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

## Extra 

Coming soon.

## Sources

Coming soon.