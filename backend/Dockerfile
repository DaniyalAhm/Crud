# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y curl software-properties-common

# Install Node.js (including npm)
RUN apt-get update





RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
	

RUN pip3 install Flask --break-system-packages


EXPOSE 5000



CMD ["tail", "-f", "/dev/null"]












