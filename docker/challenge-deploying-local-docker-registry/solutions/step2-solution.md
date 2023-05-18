# Solution

1. Pull an image from Docker Hub:

```bash
docker pull hello-world
```

2. Create a new tag for the image using our registry:

```bash
docker tag hello-world localhost:5000/hello-world
```

3. Push the image to our registry:

```bash
docker push localhost:5000/hello-world
```
