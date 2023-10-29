# Report 
[Report](https://github.com/sjkchang/CMPE272-Assignment4/blob/master/Assignment%204%20-%20Report.pdf)

# Testing the applications

## Install Docker
Docker images have been pushed to DockerHub to make the applications easiser to run without configuring all of their dependencies on your system. If you do not already have docker on your systems, follow instructions on how to install docker on your machine - [Install Docker](https://docs.docker.com/get-docker/)

## Clone the Repository
```
git clone https://github.com/sjkchang/CMPE272-Assignment4.git
```

## Run framework-less application
From the root directory of the cloned repository
```
cd frameworkless-flask
docker compose up
```
Should be running at http://localhost:5000
Note: If you open the link in a new tab, sometimes the socket connection doesn't get initialized. You may need to refresh the page if messages aren't being sent

To Stop the application, run
```
docker compose down
```

## Run vue-express application
From the root directory of the cloned repository
```
cd vue-express
docker compose up
```
Should be running at http://localhost:8080

To Stop the application, run
```
docker compose down
```
