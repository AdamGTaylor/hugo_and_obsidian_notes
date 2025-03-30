# Hugo static site for Obsidian Note Hosting

Hugo static site and helper scripts for Obsidian Note Hosting

## How to use

To make the experince more seamless, this repository provides a contanized solution. You just simply have to:
``` bash
cd docker/
docker-compose build && docker-compose up -d
```
---

## Goal

The goal is to create a collection of scripts that would allow the user to create a static site with the Obsidian Notes. This makes it easier to view them while not having access to the Obsidian App itself, which for the user is not a limiting factor, but for other viewers it might be.

### Feature plan / implementation

- [X] Contenarize the application
- [ ] Add scripts to collect the desired markdown files
- [ ] Redact sensitive information present in the markdown files

These will be the main features.

---

## Further Reading

### What is Obsidian?

Obsidian is a note taking application with great extensibility. It stores its notes in a markdown format, while the plugins for it add extra functions that might be helpful for the users.

### Why Hugo?

Stepping on hugo was totally accidental but very welcomed. It is shown to be fast, while working with markdown files, that obsidian provides for us.