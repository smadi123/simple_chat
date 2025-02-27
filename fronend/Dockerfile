FROM python:3.9-slim

WORKDIR /app

# Copy the static files
COPY static /app/static
COPY .streamlit /app/.streamlit

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]