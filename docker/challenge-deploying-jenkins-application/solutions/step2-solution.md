# Solution

1. Create a file named "Dockerfile" with the following contents:

```Dockerfile
FROM jenkins/jenkins:lts
RUN jenkins-plugin-cli --plugins git matrix-auth workflow-aggregator docker-plugin
EXPOSE 8080 50000
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
```

2. To build a Docker image for Jenkins, run the following command in your terminal:

```bash
docker build -t jenkins-docker .
```
