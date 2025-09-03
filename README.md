# Debian Python Docker Container for easy development

## Pre requisites
Install Docker or Docker Desktop 
Install Visual Studio Code 
Download repository into a folder 

## Instalation Instructions
Open folder in VS Code 
Click Run -> terminal in VS Code 
Run the following command in the terminal 

> docker-compose up

Open CMD or Terminal in the host OS and run 
> docker ps -a 

Note the container ID for the PythonUdemy app 
To access the containers shell run 
> docker exec -it <CONTAINER_ID> sh

Update apt-get 

then visit localhost:8080 to view the running hello world applicaiton 

