# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port for Flask (if applicable)
EXPOSE 5000

# Set environment variables for Coolify
ENV ENVIRONMENT=""

# Use a shell command to run both Python scripts concurrently
CMD ["sh", "-c", "python html_test_app.py"]
