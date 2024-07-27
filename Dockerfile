FROM python:3.10-slim-bullseye

# Set the working directory
WORKDIR /app

COPY requirements.txt /app


# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the application code
COPY . /app


# Run the application
ENTRYPOINT [ "sh" , "entrypoint.sh"]