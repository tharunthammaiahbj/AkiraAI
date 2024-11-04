FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install the packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browser binaries
RUN playwright install 

# The container will be ready for development once dependencies are installed
