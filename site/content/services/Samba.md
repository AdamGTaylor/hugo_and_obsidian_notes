---
title: "Samba"
date: 2025-03-30
draft: false
tags: ["Samba", "filesharing", "guide"]
categories: ["service"]
---
## Description
1Samba is an old service that was made to share files among machines (printers included).

It is simple to setup and nowadays windows file explorer handles it very well. These shares can be even mounted and it is quite response while also having authentication.

## Dependency
The list of dependency is short but is the following:
- avahi
- smbclient
- machine that can be reached

### How to set it up
This will be a system service that you will be running on your host machine. 

## Extra
### Mounting on Windows
You can mount these samba share on windows as a normal drive if you have given credentials to it as (and replace user to your actual user):
```powershell
PS > $password = Read-Host -AsSecureString 
PS > New-LocalUser -Name “user” -Password $password
```
And mount by:
```powershell
PS > NET USE M: \\<ip of your machine>\location
```

You can also use a GUI, file explorer to mount the actual samba instance, but it takes a bit longer.

### VPN (tailscale)

Normally the samba share is reachable from the local network. The tailscale network through an exit node allows the user to appear as the tailnet network's exit node. The problem is that the samba share is not reachable through that.

https://superuser.com/questions/1125438/windows-10-password-error-with-samba-share

## Sources

Coming soon.