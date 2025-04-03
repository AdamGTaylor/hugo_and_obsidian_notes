---
title: "Mosquitto"
date: 2025-04-03
draft: false
tags: ["MQTT", "guide"]
categories: ["service"]
---
## Description

Mosquitto is an MQTT services which can be self hosted with the official docker image. An MQTT service is consisting of a host (this container) and devices that subscribing and publishing to defined topics under it.

# How to Set it up

As usual, I went with the docker image.

### Docker-compose file

Here is the docker-compose file I am using for the project.
``` yaml
services:
  mosquitto:
    image: eclipse-mosquitto:latest
    container_name: mosquitto
    restart: always
    ports:
      - '1883:1883' # Communicatio
      - '9001:9001' # Admin panel
    volumes:
      - ../eclipse-mosquitto/config:/mosquitto/config
      - ../Deployment/eclipse-mosquitto/data:/mosquitto/data
      - ../Deployment/eclipse-mosquitto/log:/mosquitto/log
```

Now we just need to add devices that can communicate with it.
## Extra

Coming soon.

## Sources

Coming soon.