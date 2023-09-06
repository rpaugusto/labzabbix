# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY ./app /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port that the Flask application will run on
EXPOSE 5000

# Run the Flask application when the container starts
CMD ["python", "fake_metrics.py"]
