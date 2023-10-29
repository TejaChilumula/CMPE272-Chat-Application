FROM python:3.8-alpine
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install flask flask-socketio


ENTRYPOINT [ "python" ]
CMD [ "server.py"]
EXPOSE 5000
