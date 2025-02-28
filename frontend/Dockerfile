FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for static files
RUN mkdir -p /app/static/fonts

# Don't copy application code - it will be mounted as a volume
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.runOnSave=true", "--server.fileWatcherType=poll"]