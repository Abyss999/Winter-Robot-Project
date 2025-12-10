FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first
COPY ../requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]