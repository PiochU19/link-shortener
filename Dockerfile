# Import a base image

FROM python:3


# Environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Create a working directory

WORKDIR /code


# Copy requirements

COPY requirements.txt /code/


# Install requirements

RUN pip install -r requirements.txt


# Copy the project files into the working directory

COPY . /code/


# Open a port on the container

EXPOSE 8000