# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container (optional, if you want to use /app)
WORKDIR /app

# Copy the necessary files into the container (make sure paths are correct)
COPY requirements.txt /app/
COPY model /app/model/
COPY server /app/server/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the new port
EXPOSE 8000

# Set the command to run the server
CMD ["python", "server/server.py"]
