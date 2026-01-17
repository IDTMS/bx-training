FROM python:3.11-slim

WORKDIR /app
COPY agent.py /app/agent.py

RUN pip install --no-cache-dir --upgrade pip

ENV PYTHONUNBUFFERED=1
CMD ["python", "agent.py"]
