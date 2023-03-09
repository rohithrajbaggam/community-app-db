FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy project files
COPY . /app/

WORKDIR /app
