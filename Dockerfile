FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask requests
COPY exporter.py .
EXPOSE 9000
CMD ["python", "exporter.py"]
