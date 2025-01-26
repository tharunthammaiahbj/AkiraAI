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

# Install system dependencies required for ChromeDriver and Google Chrome
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gnupg \
    unzip \
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
    libatspi2.0-0 \
    redis-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

# Add Google's public signing key and Chrome repository
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update

# Install Google Chrome version 131.0.6778.85
RUN apt-get install -y google-chrome-stable=132.0.6834.110-1  && \
    apt-mark hold google-chrome-stable  # Prevent auto-upgrades

# Install ChromeDriver from the official Chrome for Testing repository
RUN wget https://storage.googleapis.com/chrome-for-testing-public/132.0.6834.110/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip -d /usr/local/bin/ \
    && mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/ \
    && rm -r /usr/local/bin/chromedriver-linux64 chromedriver-linux64.zip \
    && chmod +x /usr/local/bin/chromedriver


# Ensure the necessary directories are created for Playwright if needed
RUN mkdir -p /home/vscode/.cache/ms-playwright && \
    PLAYWRIGHT_BROWSERS_PATH=/home/vscode/.cache/ms-playwright playwright install chromium --force && \
    rm -rf /var/lib/apt/lists/* /tmp/*

# Set environment variables
ENV PYTHONPATH=/workspace/AkiraAI

# Set a writable cache directory for Hugging Face
# Set the environment variable for the cache
ENV HF_HOME=/home/vscode/.cache/huggingface/hub

# Ensure the directory exists and is writable
RUN mkdir -p /home/vscode/.cache/huggingface/hub && \
    chown -R vscode:vscode /home/vscode/.cache/huggingface
