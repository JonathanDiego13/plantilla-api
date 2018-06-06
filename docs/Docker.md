#### [Install and configure](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository)
#### Create image and run container
```
pull python image: docker pull python:3.6
build project's image: docker build . -t <tag>:<version>
run image:
    1. We need to create .env file similar to .env in web/config, without the export part
    2. docker run -p=<host_port>:<docker_port> --env-file=path_to_dotenv_file <tag>:<version>
```

**run in development environment**

```
docker run -it --entrypoint=/code/Docker/entrypoint-develop.sh -p=<host_port>:<docker_port>
 --env-file=path_to_dotenv_file <tag>:<version>
 ```
