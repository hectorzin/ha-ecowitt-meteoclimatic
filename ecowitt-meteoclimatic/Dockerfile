# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Install necessary dependencies
RUN apk update && apk add --no-cache \
    git \
    jq \
    bash \
	curl

RUN mkdir -p ecowitt-meteoclimatic
# Install project dependencies
WORKDIR /ecowitt-meteoclimatic

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /ecowitt-meteoclimatic/
RUN pip install --no-cache-dir -r requirements.txt

# Copy run.sh into the working directory
COPY run.sh /ecowitt-meteoclimatic/
COPY main.py /ecowitt-meteoclimatic/

# Ensure the script has execution permissions
RUN chmod +x /ecowitt-meteoclimatic/run.sh

WORKDIR /ecowitt-meteoclimatic
EXPOSE 8124
# Run the application using run.sh
CMD [ "bash", "/ecowitt-meteoclimatic/run.sh" ]
