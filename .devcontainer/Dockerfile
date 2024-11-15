# Use a Python-based image from the official Docker repository
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install the required dependencies for the project
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the necessary directories are created if they don't exist
RUN mkdir -p /home/vscode/.cache/ms-playwright
RUN PLAYWRIGHT_BROWSERS_PATH=/home/vscode/.cache/ms-playwright playwright install chromium --force

# Install system dependencies required for Playwright's Chromium browser
RUN apt-get update && apt-get install -y \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    libatspi2.0-0 

