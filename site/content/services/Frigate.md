---
title: "Frigate"
date: 2025-04-02
draft: false
tags: ["NVR", "security", "guide"]
categories: ["service"]
---
## Description

Frigate is an NVR (network video recorder) application / service. To make it easily understandable: Frigate will collect the video streams of the cameras that you are told it to use and it will apply necessary functions / methods to handle these videostreams. These functions would be like different object detections, detecting movement, making a recording and storing it.

## Functions

### *Snapshots*
It is possible to record the videostreams or pictures when something happens. These are made available under a different option, timeline.

### *Object detection*
Different object types can be detect in the available streams. This can be solved with using a CPU detector, meaning our model runs on the CPU. This is not optimal, further solutions are there to ease the weight on the CPU: GPUs and TPUs can be used to run these models, while the integrated GPU in the CPU could be used to decode the streams.

Personal taste: I got a Coral TPU (USB-C) that can be used to speed up the model's inference. It's another story how hard it is to update it.

## How to Set it up
As usual, I went it the docker container and the docker-compose file.

### Docker-compose file
```yaml
services:
  frigate:
    container_name: frigate
    privileged: true # this may not be necessary for all setups
    restart: unless-stopped
    image: ghcr.io/blakeblackshear/frigate:stable
    cpuset: "2,3,4,5"
    shm_size: "64mb"
    devices:
      - /dev/dri/renderD128 # for intel hwaccel, needs to be updated for your hardware
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - ../config:/config
      - ../storage:/media/frigate
      - type: tmpfs # Optional: 1GB of memory, reduces SSD/SD Card wear
        target: /tmp/cache
        tmpfs:
          size: 1000000000
    ports:
      - "5000:5000"
      - "8554:8554" # RTSP feeds
      - "8555:8555/tcp" # WebRTC over tcp
      - "8555:8555/udp" # WebRTC over udp
    environment:
      FRIGATE_RTSP_PASSWORD: "XXX"
```
This compose file contains the usual stuff, but a couple of extras are there:
- **privileged**: it allows docker to bypass some checks and in my case it was needed to access the Coral TPU USB-C I was using. 
- **devices: /dev/dri/renderD128**: This the integrated GPU in the processor, which is not powerful, but good enough to speed up ffmpeg.

### Config file

Coming soon.
## Extra

### Note on TCP traffic and Ports
The only problem allowing tcp communication is that the packages can arrive in a different order than what is intended. In the case of an NVR, this could pose an issue as frames arriving in a different order than what is intended results to incorrect recordings.

## Sources

Coming soon.
