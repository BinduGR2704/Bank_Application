# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]

# ENV FLASK_APP=app.py
# ENV FLASK_ENV=development

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]