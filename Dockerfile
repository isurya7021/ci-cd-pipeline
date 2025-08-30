# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy your application code
COPY app.py /app/app.py

# Run the app when the container starts
CMD ["python", "app.py"]

