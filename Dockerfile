# Use an official Python runtime as a parent image      
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Clone the GitHub repository
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/yoyitowang/NLpillow.git

WORKDIR /app/NLpillow

# Install any dependencies your Python project may have
RUN pip install -r requirements.txt

# Run your Python application
CMD ["python", "main.py"]