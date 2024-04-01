# Use official Python runtime as base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code to the container
COPY . .

# Install Flask and other dependencies
RUN pip install Flask flask-cors

# Expose the port the app runs on
EXPOSE 5001

# Define the command to run the Flask app
CMD ["python", "server-2.py"]
