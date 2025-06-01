# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application code and requirements
COPY app/ /app/
COPY app/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the app's port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
