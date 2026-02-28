# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole application
COPY inventory_app/ ./inventory_app

# Set environment variables
ENV PYTHONPATH=/app/inventory_app

# Expose FastAPI port
EXPOSE 4000

# Run the app with uvicorn
CMD ["uvicorn", "inventory_app.main:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]