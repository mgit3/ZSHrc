# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Create a non-root user and switch to that user
RUN useradd --create-home appuser
USER appuser

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN python -m pip install --user --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]
