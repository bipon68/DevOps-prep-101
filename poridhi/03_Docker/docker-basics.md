### Docker Basics

#### Terms
- Client/server architechture
- Hypervisors
- Containers
- Images
- Dockerfiels
- Kernel
- Docker daemon(engine)
- process
- Docker registries
- Virtual machines

#### Summary
- Docker is a platform for consistently building, running, and shipping applications. 
- A virtual machine is an abstraction of hardware resources. Using hypervisors we can create and manage virtual machines. The most popular hypervisors are VirtualBox, VMware and Hyper-v (Windows-only).
- A container is an isolated environment for running an application. It’s essentially an operating-system process with its own file system. 
- Virtual machines are very resource intensive and slow to start. Containers are very lightweight and start quickly because they share the kernel of the host (which is already started). 
- A kernel is the core of an operating system. It’s the part that manages applications and hardware resources.  Different operating system kernels have different APIs. That’s why we cannot run a Windows application on Linux because under the hood, that application needs to talk to a Windows kernel. 
- Windows 10 now includes a Linux kernel in addition to the Windows kernel. So we can run Linux applications natively on Windows. 
- Docker uses client/server architecture. It has a client component that talks to the server using a RESTful API. The server is also called the Docker engine (or daemon) runs in the background and is responsible for doing the actual work.
- Using Docker, we can bundle an application into an image. Once we have an image, we can run it on any machine that runs Docker. 
- An image is a bundle of everything needed to run an application. That includes a cutdown OS, a runtime environment (eg Node, Python, etc), application files, third-party libraries, environment variables, etc.
- To bundle an application into an image, we need to create a Dockerfile. A Dockerfile contains all the instructions needed to package up an application into an image.
- We can share our images by publishing them on Docker registries. The most popular Docker registry is Docker Hub