# The Java service implementation

This repo contains a small [Spring Boot](https://spring.io/projects/spring-boot) application containing the initial API endpoints.

## Setup

Clone the repo, make sure you have Java installed, we recommend AdoptOpenJDK version 8 or version 11.

### Launch the application

MacOS/Linux:
```
./mvnw spring-boot:run
```

Windows:
```
mvnw spring-boot:run
```

You will a Comcast banner and start up message showing the application listening for requests on localhost port 8080.

## Testing Your Local Server

Using `curl` send the following test request to the spring boot application.

MacOS/Linux:
```
➜ curl -id '{"input":"Comcast is best place to work!"}' -H 'Content-Type: application/json' http://localhost:8080/stringinate
```
Windows:
```
curl -i -X POST -H "Content-Type:application/json" -d "{\"input\": \"Comcast is best place to work!\" }" http://localhost:8080/stringinate
```

If the application is running you should see the following output in your terminal:

```
HTTP/1.1 200
Content-Type: application/json
Transfer-Encoding: chunked
Date: Sat, 05 Jun 2021 12:03:31 GMT

{"input":"Comcast is best place to work!","length":30}
```
