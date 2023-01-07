#the latest python base image
FROM python:latest

#create app folder
WORKDIR /app

#copy python files to app directory
COPY /src ./app
