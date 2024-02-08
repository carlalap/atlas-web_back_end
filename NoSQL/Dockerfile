FROM python:3.8

# Update package lists and install essential packages
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    git \
    tar \
    vim \
    emacs \
    build-essential \
    gcc \
    locales

# Install MongoDB
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list && \
    apt-get update && \
    apt-get install -y mongodb-org && \
    mkdir -p /data/db

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install pytz pymongo

# Set the locale
RUN locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

# Create and set permissions for the /NoSQL directory
RUN mkdir -p /NoSQL && \
    chmod -R 777 /NoSQL

# Expose MongoDB port
EXPOSE 27017

# Start MongoDB service
CMD ["/usr/bin/mongod", "--fork", "--logpath", "/var/log/mongodb/mongod.log", "--bind_ip_all"]
