FROM golang:alpine

COPY *.go *.sh /app/

WORKDIR /app

CMD [ "sh", "-u", "iterate.sh" ]