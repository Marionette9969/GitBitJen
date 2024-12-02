# Step 1: Use an official Python runtime as the base image
FROM python:3.11.10-slim

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Step 2: Set the working directory in the container
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    libx11-dev \
    libx264-dev \
    libfontconfig1 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libnss3 \
    libasound2 \
    chromium \
    --fix-missing \
    && rm -rf /var/lib/apt/lists/*


# Step 3: Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the application code
COPY . .

# Step 5: Expose the port the app will run on
EXPOSE 5000

# Step 6: Define the command to run the app
CMD ["python", "app.py"]