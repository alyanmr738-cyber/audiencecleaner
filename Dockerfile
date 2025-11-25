FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements_web.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements_web.txt

# Copy application files
COPY app.py .
COPY clean_audience.py .

# Create directories for temp files
RUN mkdir -p /tmp/uploads /tmp/outputs

# Expose port
EXPOSE 5000

# Set environment variables
ENV PORT=5000
ENV DEBUG=False

# Run the application
CMD ["python", "app.py"]

