# Debian Python Docker Container for easy development

## Pre requisites
Install Docker or Docker Desktop <br>
Install Visual Studio Code <br>
Download repository into a folder <br>

## Instalation Instructions
Open folder in VS Code <br>
Click Run -> terminal in VS Code <br>
Run the following command in the terminal <br>

> docker-compose up

Open CMD or Terminal in the host OS and run <br>
> docker ps -a 

Note the container ID for the PythonUdemy app <br>
To access the containers shell run <br>
> docker exec -it <CONTAINER_ID> sh

Update apt-get <br>

then visit localhost:8080 to view the running hello world applicaiton <br>

