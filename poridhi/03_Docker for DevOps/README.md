# Docker - Module Three

**Docker**
- [ ] 01 - Class 1
	- Docker Introduction
	- Basic Concepts
	- Hands-On
	- Writing Dockerfile Smartly
- [ ] 02 - Class 2
	- Docker Networking Internals
- [ ] 03 - Class 3
	- Docker-based MySQL replication
- [ ] 04 - Class 4
	- Redis & Kafka deployment and integration
- [ ] 05 - Class 5
	- ElasticSearch deployment and integration
	- Nginx Layer 4 & 7
	- Load Balancer
- [ ] 06 - Class 6
	- Docker Compose 
	- Full Stack Application Deployment 


### Reference
- [Install Docker](https://docs.docker.com/desktop/install/windows-install/)
- [Docker playground](https://labs.play-with-docker.com/)

### Docker command
- Syntax and usage of the Docker build command `docker build [OPTIONS] PATH | URL` `docker build -t imagename DockerfilePath`
- Docker engine `systemctl status docker`
- create a container `sudo docker run hello-world`
- running container show `sudo docker ps` `sudo docker ps -a` stop container `sudo docker stop web01 nginx`
- create a new container `sudo docker run --name web01 -d -p 9080:80 nginx` `sudo docker inspect web01` `ip addr show`
- build  `docker build -t hello-world .` create a image. `docker image ls` list view `ls -1` `ls -l` 
- tag added `docker image -t react-app:dev .` `docker image tag react-app:latest react-app:1` `docker image tag 149ad6b6c9bd react-app:latest` `docker image tag 149 bipon68/react-app:2`
`docker image tag react-app:3 bipon68/react-app:3`
- push `docker push bipon68/react-app:2` at first login `docker login` then push new tag `docker image tag react-app:3 bipon68/react-app:3` `docker push bipon68/react-app:3`
- image remove `docker image remove react-app:dev`
- image show `docker image ls`  env show `printenv`
- image run  `docker run hello-world` run into container `docker run -it react-app` `docker run -it react-app sh` 
- pull image  `docker pull bipon68/hello-world`
- run image  `docker run bipon68/hello-world`
- container show `docker ps` `docker ps -a` start a container `docker start -i 0202e3b8ebe4`
- removed unknone tag image or stopped container `docker container prune` then `docker image prune` Remove unused images. remove single image `docker image rm 149ad6b6c9bd`
- going to root for Linux `docker run -it ubuntu` container run into interactive mood
- process show `ps` running container show`docker ps` all container show `docker ps -a`
- docker image help `docker image --help` `docker load --help` `docker save --help`
- save image `docker image save -o react-app.tar react-app:3`
- load image `docker image load -i react-app.tar`
- container run `docker run -d react-app` `docker run -d --name bluy-sky react-app`
- container logs <docker logs <containerID>> `docker logs ff1d4dbce853` `docker logs -n 5 ff1d4dbce853` `docker logs -n 5 -t ff1d4dbce853`
- publishing port `docker run -d -p 80:3000 --name c1 react-app`
- execution command `docker exec c1 ls` `docker exec -it c1 sh`
- container start and stop `dokcer stop c1` `dokcer start c1` 
- container remove `docker rm c1` `docker rm -f ch1`
- filter `ls | grep data
- volume `docker volume create app-data` `docker volume inspect app-data` `docker run -d -p 4000:3001 -v app-data:/app/data react-app` ` docker volume ls` `docker volume rm vidly_vidly`
- copy file container host to `docker cp 862087bfb94a:/app/log.txt` `docker cp secret.txt 862087bfb94a:/app`
- sharing the sourcecode with a container `docker run -d -p 5001:3000 -v $(pwd):/app react-app
- `docker image ls -q` only showing image id
- all container remove `docker container rm -f $(docker container ls -aq)`
- all image remove `docker image rm -f $(docker image ls -q)` 
- compose `docker compose build` `docker-compose build --no-cache`
- start and stoping application `docker-compose up` `docker-compose up -d` `docker-compose down` `docker volume ls`
- docker network `docker network ls` `docker exec -it 712 sh` `docker exec -it -u root 712 sh` `docker-compose logs --help` `docker logs 712 -f`
- reduce image size `docker build -t vidly_web_opt -f Dockerfile.prod .`
- build image optimzely `docker build -t vidly_web_opt -f Dockerfile.prod .`
- production build `docker-compose -f docker-compose.prod.yml build`
- production up `docker-compose -f docker-compose.prod.yml up -d` image rebuild `docker-compose -f docker-compose.prod.yml up -d --build`
- docker machin evn `docker-machine env vidly` `eval $(docker-machine env vidly)`
- inspect image `dokcer inspect container-name`
- Remove stop all container `docker system prune -a` 


