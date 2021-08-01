# The Python service implementation

This repo contains a small [Flask](https://flask.palletsprojects.com/) application  the initial API endpoints.

## Setup

Clone the repo, make sure you have python3 installed, and then run `./install.sh`.

Once the dependency install has completed, execute `. venv/bin/activate && ./run.sh` to launch the application.

## Testing Your Local Server

Using `curl` send the following test request to the Flask application.

```
curl -id '{"input":"this is the input"}' -H 'Content-Type: application/json' http://localhost:5000/stringinate
```

If the application is running you should see the following output in your terminal:

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 35
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Wed, 05 May 2021 13:22:16 GMT

{
  "input": "this is the input",
  "length": 17
}
```
