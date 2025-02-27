FROM python:3.9-slim

WORKDIR /app

# Create directories for static files
RUN mkdir -p /app/static/fonts

# Copy the static files and Streamlit config
COPY static/fonts/*.ttf /app/static/fonts/
COPY .streamlit /app/.streamlit

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]