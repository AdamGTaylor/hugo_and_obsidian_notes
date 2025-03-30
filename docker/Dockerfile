FROM debian:bookworm-slim

RUN apt update && apt install -y hugo

WORKDIR /app
COPY ../site /app
EXPOSE 1313
CMD ["hugo", "server", "--bind=0.0.0.0", "--baseURL=http://mynotes.local/", "--buildDrafts"]
