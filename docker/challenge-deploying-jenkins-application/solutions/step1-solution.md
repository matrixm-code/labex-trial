# Solution

To install Docker Compose on Linux, follow these steps:

1. Run the following command to download the Docker Compose binary:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

2. Run the following command to make the Docker Compose binary executable:

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

3. Verify that Docker Compose is installed by running the following command:

```bash
docker-compose --version
```
