# Use the official Python image as the base
FROM python:3.10-slim

# Install pip and Poetry
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry

# Set the working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml /app/

# Install dependencies globally using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy the application code
COPY ./blog /app

# Expose the application port
EXPOSE 8000

# Command to start the application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "500"]