---
title: "Node Exporter"
date: 2025-04-03
draft: false
tags: ["monitoring", "guide"]
categories: ["service"]
---
## Description

Node exporter is a system monitoring tool which monitors the host system and makes this information available through an API. 

## How to Set it up

In this case it would obvious that we use it as a host system service as it meant to monitor the system that is runned on. However, docker has a trick around it and this service also has a docker image.

### Docker-compose file

``` yaml
services:
  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    restart: unless-stopped
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
    ports:
      - 9100:9100
    deploy:
      resources:
        limits:
          cpus: "1"
          memory: "2G"
        reservations:
          cpus: "0.1"
          memory: "1G"
```
With volumes, we can make the different folder is our filesystem visible to the given docker image. For monitor, we would need to add critical information which we are not intended to be manipulated by anyone, but by the system itself. To limit acces, we can use ":ro" after each volume, standing for "read only".


## Extra

### Output

The output depends on the system we want it to run on, but let's just get a quick taste of it (accessing {device id}:9100/metrics):
``` log
# HELP go_gc_duration_seconds A summary of the pause duration of garbage collection cycles.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 1.5483e-05
go_gc_duration_seconds{quantile="0.25"} 1.9269e-05
go_gc_duration_seconds{quantile="0.5"} 2.3703e-05
go_gc_duration_seconds{quantile="0.75"} 5.3018e-05
go_gc_duration_seconds{quantile="1"} 8.799e-05
go_gc_duration_seconds_sum 0.360508225
go_gc_duration_seconds_count 10165
...
```
And there are like thousands of rows of this.
## Sources

Coming soon.