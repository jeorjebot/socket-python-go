# TCP Socket between Python and Go
Simple program to perform a TCP connection on a socket between **Python** and **Go**.
Both server and client applications are running inside separate **docker containers**.

## Architecture
- **Python server** -> waiting on server:8000
- **Python client** -> wait 5s, send and receive a message, repeat 2 times
- **Go client** -> wait 5s, send and receive a message, repeat 2 times

## Start the docker compose
Clone the repository, and then inside it run:
```console
docker-compose -p project up --build
```

## Python socket docs
- https://docs.python.org/3/library/socket.html

## Go socket docs
- https://golang.org/pkg/net/

