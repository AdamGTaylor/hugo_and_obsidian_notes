---
title: "Nextcloud"
date: 2025-04-03
draft: false
tags: ["office suite", "file sharing", "guide"]
categories: ["service"]
---
## Description

Nextcloud is a services, that mostly targets file sharing functionality. While this is the main goal, the Nextcloud AIO image can also be used for other application, like Qtalks and other. It's an alternative for a group for application, mainly Google Drive, Google Meet, etc...

In the following, the Nextcloud AIO image will be used.

# How to Set it up

As usual, I went with the original docker image. In this case it will be the Nextcloud AIO image.

### Docker-compose file


## Furthermore

### Optimal resources

There is a noticeable difference if you are using it through wifi. There is a bunch of applications that comes in the office suite during installation. Only pick these if your intention is to use them, otherwise they are unnecessary overhead. The optimal resources to run the image in 2 CPU cores and 4 gigabytes of RAM.

## Extra

Change some database settings:
https://docs.nextcloud.com/server/23/admin_manual/configuration_database/linux_database_configuration.html#configuring-a-mysql-or-mariadb-database

## Sources

Coming soon.