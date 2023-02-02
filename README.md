microservice2
Get weaher from given zipcode
Method 1 - run python file
![image](https://user-images.githubusercontent.com/122847154/216264337-9a437b89-25bf-4790-9a06-d1b07580ae04.png)

Method 2
Go to directory: cd ~/Desktop/Microservice2 
Build image: docker build -t microservice2:1.0 . 


Run container: docker run -d -p8000:8000 microservice2:1.0  
list all the container: docker ps -a  


Check logs, see what happening inside the container:
docker logs 4433fca810b5


Giving a tag for docker image
docker tag microservice2:1.0 jinping4038/microservice2



docker login
Store the docker image in repository 
docker push jinping4038/microservice2 



Download the docker image from the repository
docker pull jinping4038/microservice2
Run the docker image on port 8000.
docker run -d -p8000:8000 jinping4038/microservice2


http://localhost:8000/weather/94539


You can download docker images from this link givenbelow:
https://hub.docker.com/r/jinping4038/microservice2







