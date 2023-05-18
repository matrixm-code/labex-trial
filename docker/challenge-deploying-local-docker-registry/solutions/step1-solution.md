# Solution

1. Pull the Docker registry image:

```bash
docker pull registry:latest
```

2. Create a directory called `dockerregistry` in the `/home/labex` path to make it easier for the container image to persist.

```bash
mkdir dockerregistry
```

3. Run the Docker registry:

```bash
docker run -d -p 5000:5000 -v /home/labex/dockerregistry:/var/lib/registry --name my-registry registry:latest
```

4. Verify that the repository is available.

```bash
curl http://localhost:5000/v2/_catalog
```

In this command, we are running the Docker registry image as a daemon, exposing port `5000` on our local machine, naming our container `my-registry`.
