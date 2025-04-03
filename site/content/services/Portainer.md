---
title: "Portainer"
date: 2025-04-02
draft: false
tags: ["GUI", "guide"]
categories: ["service"]
---
## Description

Portainer is GUI that interracts with docker related stuff. The simple GUI not only allows simple interractions, but it is responsive to changes and through portainer agents, multiple devices can be added to our portainer stack.

## How to Set it up

As usual, I went with the official docker image.

### Docker-compose file
``` yaml
services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    ports:
      - '8000:8000'
      - '9443:9443'
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ../portainer/portainer_data:/data
    restart: always
```
## Extra

### Recommended: SSL certificate
While you are able to access this services with ip:port combination, it won't succed as portainer requires https connection. If you have a reverse-proxy solution already available (like NPM), you can quickly add it as a proxy_host with a subdomain having ssl certficiate.

### Docker version issue and access problems

In the past, there was an issue related to docker container and the interactions with them through Portainer. Due to some hidden problem, even though the GUI allows log access and login into the docker container as root. (These can be done with "docker log" and "docker exec -it our_container /bin/bash" or something similar.) It is advised to be up to date and informed about issues related to the docker images we use. As such, using the ":latest" image is somewhat not advised.

## Sources
