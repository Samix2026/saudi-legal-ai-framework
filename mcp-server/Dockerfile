FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Repo is mounted read-only at runtime via -v /path/to/repo:/repo:ro
CMD ["python", "server.py"]
