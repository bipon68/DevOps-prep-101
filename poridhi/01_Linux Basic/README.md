# Linux Basic


## Table of Contents
- [x] Namespace


### Namespace
In Linux, a namespace is a feature that allows processes to use the system resources they need but separately from other processes. A namespace is a way to virtualize a global system resource such that a process that needs it operates in an isolated instance of that resource.

Additionally, a group of resources and processes can refer to the same namespace, but each namespace has individual resources for each. Only processes in the same namespace can identify the changes made in a global resource.


## Linux Command
- root user `sudo -i`
- `ip addr show` `ip link`
- `netstat -antp` `netstat -antp | grep 749`
- `ss -tunlp`
- `dig www.google.com`
- `route -n`
- `arp`
- `mtr www.google.com`
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

### Reference
- [Namespace](https://man7.org/linux/man-pages/man7/namespaces.7.html), [list-namespaces](https://www.baeldung.com/linux/list-namespaces) 