# Use an official Python image. Autogen currently requires >= 3.8, < 3.12
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory to /app
# Actually, let's comment this out and just bind-mount it
#COPY . /app

# Install vim
RUN apt update
RUN apt install vim git --assume-yes

# Install required packages
RUN pip install --trusted-host pypi.python.org pyautogen docker aider-chat

# Suppress exception for "dubious ownership" of git repo
RUN git init
RUN git config --global --add safe.directory /app

# Default command
CMD ["/bin/bash"]
