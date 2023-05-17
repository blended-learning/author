# Users

*users.<group>* is the userfile, with the format as follows:

```
ID  username   password
```

# Remote key

- Leave it to the user to create access

# CPU limit

# Memory limit

# SSH port

# Local storage

# Docker image

```
docker run -it --rm --name <name>
    --cpus <cpu>
    --memory <memory>
    -p <port>:22
    -v <userfile>:/etc/<userfile>
    -v <home>:/home
```