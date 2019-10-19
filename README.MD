# DEXMA DevOps / System Engineer Test

## Introduction

We need to deploy a microservice (created by our developer team in python) to production that help us to monitorize the status of a new instance of RedisDB.

## Architecture
This architecture will have two components:

* RedisDB Server 
* Web Application (Code provided)

## RedisDB Server
To test this new microservice, you need to install a redisDB instance with the following requirements:

* Authentication is required, so you need to configured it with password. 

## Web Application 

You already have the code of the application, the only thing you need to do provide this three environment variables: 

* $REDIS_HOST: Host to connect with redis
* $REDIS_PORT: Port where is listen the db 
* $REDIS_PASSWORD: Password you set on redis configuration

This microservice will listen on port 8081 (by default) and will respond for the following endpoints:

* /ping
* /redis-status

Also you need to install all the dependencies, this packages are in requirements.txt file.

# Deployment

Using docker and docker-compose, doing **docker-compose up** we want to deploy all the required infrastructure for this application to work. 
After the application is working, we should get the following result:

```
$ curl -L http://localhost:8081/ping
pong
$ curl -L  http://localhost:8081/redis-status
{"redis_connectivity": "OK"}
```

The provided solution should be updated to a public GitHub, GitLab, Bitbucket repository with :

* Dockerfiles
* docker-compose File
