FROM debian:bookworm-slim

# Get basic installs
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    bash \
    tar 

# Set Hugo version
ENV HUGO_VERSION="0.125.7"

# Download and install Hugo
RUN curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" -o hugo.tar.gz \
    && tar -xzf hugo.tar.gz \
    && mv hugo /usr/local/bin/hugo \
    && rm hugo.tar.gz

# Prepare app dir
WORKDIR /app
RUN mkdir /ws
COPY ../site /app
COPY ../.env /app
COPY ../docker/entrypoint.sh /ws

# Make sure the script is executable
RUN chmod +x /ws/entrypoint.sh

# Use the entrypoint script
ENTRYPOINT ["/ws/entrypoint.sh"]