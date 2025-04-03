---
title: "Syncthing"
date: 2025-04-03
draft: false
tags: ["file sharing", "guide"]
categories: ["service"]
---
## Description

Syncthing is a two-way file syncing service, similar to [[Nextcloud]], but it's more decentralized with limitation of the number of connected devices. It also has an official android and windows app that also supports browser GUI. The android app has been discontinued with the date of 4th of December, 2024. (f-droid fork option is available).

Main features:
- Decentralized
- Encrypted
- Lightweight

## How to Set it up

As usual, I went with the official docker image.

### Docker-compose file

``` yaml
services:
  syncthing:
    image: lscr.io/linuxserver/syncthing:latest
    container_name: syncthing
    hostname: syncthing #optional
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ../syncthing/config:/config
      - ../syncthing_data:/data1
    ports:
      - 8384:8384
      - 22000:22000/tcp
      - 22000:22000/udp
      - 21027:21027/udp
    restart: unless-stopped
```


## Extra

### Setting login

When you start this image and login for the first time, it will complain about having no authentication as a security issue. Setting a username and password to it should be a priority. 
## Sources

Coming soon.