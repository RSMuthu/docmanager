FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the application code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["poetry", "run", "fastapi", "dev", "api/main.py"]
