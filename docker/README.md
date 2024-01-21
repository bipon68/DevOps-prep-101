# Docker


### Reference
- [Install Docker](https://docs.docker.com/desktop/install/windows-install/)
- [Docker playground](https://labs.play-with-docker.com/)

### Docker command

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

### Linux command
- create folder `mkdir test`
- rename folder name `mv test docker` output `docker`
- create new file `touch hello.txt` create multiple file `touch file1.txt file2.txt file3.txt`
- rename filename `mv hello.txt hello-docker.txt` output `hello-docker.txt`
- remove file `rm file1.txt file2.txt` `rm file*` remove directory `rm -r docker`
- package install `apt install nano` `apt` (advance package tool) package manager in ubuntu `nano` is a package. `nano` is a basic text editor in Linux. `nano file1.txt`
- `apt update` update the package database
- `cat file1.txt` showing `file1.txt` content of this file.
- write a user in `.bashrc` `echo DB_USER=bipon >> .bashrc` `source .bashrc` shoting data in home directory otherwise have to go in terminal. 
- user create `useradd -m bipon` `useradd bipon`  help `useradd` show user `cat /etc/passwd` few user command `useradd usermod groupadd` few example `usermod -s /bin/bash bipon` `cat /etc/shadow`
- create group `groupadd js` added a member in a group `usermod -aG js bipon` `addgroup app` `adduser -S -G app app` group show `groups app` multiple command `addgroup bipon && adduser -S -G bipon bipon` show userlist `cat /etc/passwd`
- create directory `mkdir dev` file create `touch demo.txt` showing file `ls dev` output `file1.txt file2.txt file3.txt`
- file permission `chown bipon:js dev/file1.txt` permission modification `chmod 700 dev/file3.txt`
- copy file `cp dev2/file4.txt dev` move `mv dev2/file5.txt dev` rename `mv dev2/file6.txt dev2/file66.txt` remove directory `rm -r dev2`
- write something into a file `echo "Hello World" > dev2/file4.txt` file read `cat dev2/file4.txt`
- data show in long `ls -l`


