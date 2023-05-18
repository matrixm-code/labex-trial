# Solution

1. Deleted the image:

```bash
docker rmi localhost:5000/hello-world
```

2. Pull the image from the registry:

```bash
docker pull localhost:5000/hello-world
```

3. Run the container for the image you just pulled:

```bash
docker run localhost:5000/hello-world
```
