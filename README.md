# microservice2 - Get weaher from given zipcode
Steps:

pdffile:
[Microservice2.pdf](https://github.com/Jinping4038/Microservice2/files/10566475/Microservice2.pdf)

Method 1 - run python file
![image](https://user-images.githubusercontent.com/122847154/216264337-9a437b89-25bf-4790-9a06-d1b07580ae04.png)

Method 2
Go to directory: cd ~/Desktop/Microservice2 
Build image: docker build -t microservice2:1.0 . 
![image](https://user-images.githubusercontent.com/122847154/216264459-fb923283-9347-403f-9efb-7e11c39ef0bf.png)


Run container: docker run -d -p8000:8000 microservice2:1.0  
list all the container: docker ps -a  
![image](https://user-images.githubusercontent.com/122847154/216264519-e256e67d-155a-4d7a-a8e7-bf9972657870.png)


Check logs, see what happening inside the container:
docker logs 4433fca810b5

![image](https://user-images.githubusercontent.com/122847154/216264562-66646c62-f3a5-4e3b-ba67-2deebbd0b642.png)
![image](https://user-images.githubusercontent.com/122847154/216264589-afe80510-0405-48b0-843a-60ecf0543718.png)

Giving a tag for docker image
docker tag microservice2:1.0 jinping4038/microservice2
![image](https://user-images.githubusercontent.com/122847154/216264612-8596151d-5814-473b-8566-6f0d4b03eb6f.png)



docker login
Store the docker image in repository 
docker push jinping4038/microservice2 
![image](https://user-images.githubusercontent.com/122847154/216264636-ce464f84-e8f7-4d78-b57a-8ddcb56db14f.png)




Download the docker image from the repository
docker pull jinping4038/microservice2
Run the docker image on port 8000.
docker run -d -p8000:8000 jinping4038/microservice2
![image](https://user-images.githubusercontent.com/122847154/216264658-9ad76e09-439f-413f-bc04-5171843736af.png)

http://localhost:8000/weather/94539
![image](https://user-images.githubusercontent.com/122847154/216264696-91a011f5-5bb9-449f-867f-3e73564cdfd4.png)


You can download docker images from this link givenbelow:
https://hub.docker.com/r/jinping4038/microservice2

![image](https://user-images.githubusercontent.com/122847154/216264749-10ade469-86a7-47d0-b2cb-5013f0538080.png)






