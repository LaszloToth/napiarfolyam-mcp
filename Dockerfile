
FROM python:3.11-slim

WORKDIR /app

COPY handler.py mcp.json requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

