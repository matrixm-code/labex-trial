# Solution

1. Create a file named "docker-compose.yml" with the following contents:

```yml
version: "3"
services:
  jenkins:
    image: jenkins-docker
    container_name: jenkins-docker
    volumes:
      - jenkins-data:/var/jenkins_home
    ports:
      - 8080:8080
      - 50000:50000
    networks:
      - jenkins
volumes:
  jenkins-data:
networks:
  jenkins:
```

2. To run Jenkins in a Docker container using Docker Compose, run the following command in your terminal:

```bash
docker-compose up -d
```
