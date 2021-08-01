# The GoLang service implementation

This repo contains a small [Echo](https://echo.labstack.com/) application containing the initial API endpoints.

## Setup

Clone the repo, make sure you have golang => 1.16 installed, and then run `./install.sh`.

Once the dependency install has completed, execute `./run.sh` to launch the application.

## Testing Your Local Server

Using `curl` send the following test request to the Flask application.

```
curl -id '{"input":"this is the input"}' -H 'Content-Type: application/json' http://localhost:1323/stringinate
```

If the application is running you should see the following output in your terminal:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Date: Mon, 07 Jun 2021 14:58:57 GMT
Content-Length: 42

{"input":"this is the input","length":17}
```