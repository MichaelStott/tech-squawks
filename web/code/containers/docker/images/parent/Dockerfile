# Use Ubuntu as base image for container
FROM ubuntu:23.04

# Install latest packages
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8


# Copy local text file into container
COPY message.txt message.txt

# Print message from file
ENTRYPOINT [ "cat", "message.txt" ]