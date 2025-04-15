---
title: "ESPHome"
date: 2025-04-03
draft: false
tags: ["microcontroller", "updater", "smart home" , "guide"]
categories: ["service"]
---
## Description

ESPHome is a simple but magnificent open source application that is used to handle esperssif's devices. These little microcontrollers are coming with BLE/WiFi and as such Over the Air (OTA) updates are available for them. ESPHome handlis this part very well. This application can be used with a docker container and official docker image exists for it. 

What really shines in it is that rather than writing C/C++ code, it uses .yaml files to handle each device. While this is convinient, we are not barred from using C/C++ code as it can be passed with as string to it.

## How to Set it up

### Docker-compose file
``` yaml
services:
  esphome:
    container_name: esphome
    image: esphome/esphome
    #ports:
    #  - '6052:6052'
    #  - '6053:6053'
    #  - '6123:6123'
    volumes:
      - ../esphome/config:/config
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
    privileged: true
    network_mode: host
```
There are officially stated ports which will be used with image, but as it is indicated, I commented them out. They not needed when the image runs with "network_mode: host" and "priviliged: true". 

## Extra

Coming soon.
## Sources

Coming soon.