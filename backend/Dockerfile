# Stage 1: Pull the model
FROM ollama/ollama:latest as builder

# Set environment variables (OLLAMA_HOST is important here for the pull to work)
ENV OLLAMA_HOST=0.0.0.0:11434

# Install any necessary dependencies
RUN apt-get update && apt-get install -y curl

# Start Ollama server in the background
RUN mkdir -p /root/.ollama
RUN nohup ollama serve > /var/log/ollama.log 2>&1 & \
    # Wait for Ollama server to start
    sleep 10 && \
    # Pull the DeepSeek model
    ollama pull deepseek-r1:14b && \
    # Give some time for the model to be fully downloaded and processed
    sleep 30

# Stage 2: Create the final image
FROM ollama/ollama:latest

# Set environment variables for Ollama (adjust as needed)
ENV OLLAMA_HOST=0.0.0.0:11434
ENV OLLAMA_ORIGINS=*

# Copy the downloaded model from the builder stage
COPY --from=builder /root/.ollama /root/.ollama

# Expose the default Ollama port
EXPOSE 11434

# Map a local repository to persist and save a local copy of the model
VOLUME ["/local/repository:/root/.ollama"]

# Add a volume for /data
VOLUME /data

# Set the entrypoint to start the Ollama server
ENTRYPOINT ["ollama"]
CMD ["serve"]