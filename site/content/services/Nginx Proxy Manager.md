---
title: "Nginx Proxy Manager"
date: 2025-04-02
draft: false
tags: ["NPM", "reverse proxy", "guide"]
categories: ["service"]
---
## Description

Nginx proxy manager (NPM) is a simple reverse proxy server with a web GUI. It also support Let's encrypt to give out SSL certificates. 

## Dependency

Depending on the way it will deployed, it requires different methods and packages to use it. I went with docker and docker image as everything is in it. 

### How to set it up

To get the docker working, plenty of examples are present and as such this will be one of many good solution.

### Docker-compose file

Here is the docker-compose file I am using for the project.
```yaml
services:
  npm:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    cpuset: "0,1"
    ports:
      - '80:80'
      - '81:81'
      - '443:443'
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    networks:
      - proxy
    deploy:
      resources:
        limits:
          cpus: "1.25"
          memory: "1G"
        reservations:
          cpus: "0.5"
          memory: "0.5G"

```
This file is somewhat matured and tailored for my needs, but has the following:
- cpuset: defines which core/thread is allowed to be used
- networks: this is an external network
- deploy/resources: gives limitations to and reservations to the docker container.

## Extra

### Depends On: NPM
Good tip: as i am using it as a reverse proxy and as such I have subdomains setup with it as "Proxy Hosts". This leads to implicit dependencies of the other services that relates them to NPM. Setting a "depends_on" in other docker services on NPM will ease any issue related to routing.

### Let's Encrypt
NPM comes with certbot already in the docker image. It is rather easy to setup and adds SSL certificate. The GUI makes it even easier and if setup correctly, it can be added to the "Proxy Hosts". 

#### Why is this good?
Well, some services that you may host in the near future require SSL certificates to function properly like Nextcloud. 

## Sources

Coming soon.