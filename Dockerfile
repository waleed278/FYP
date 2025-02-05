FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
COPY model /app/model/
COPY server /app/server/
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 8000
CMD ["python", "server/server.py"]
