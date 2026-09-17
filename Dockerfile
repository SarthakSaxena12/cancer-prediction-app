# base image
FROM python:3.11-slim

# working directory
WORKDIR /app

# requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# application code
COPY . .

# expose the application port
EXPOSE 8000

# start FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]