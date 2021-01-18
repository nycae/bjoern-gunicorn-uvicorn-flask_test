# ASGI/WSGI server test

There are plenty asgi and wsgi alternatives to serve your python apps in production, this repo tests the speed of three of the most well-known alternatives.

Keep in mind that this test is planned to test the speed at extreme conditions, that is, for the test, there were theoretically infinite requests to attend.

## Servers tested

* [Bjoern](https://github.com/jonashaag/bjoern): A C-implemented WSGI server, that should be the fastest of the bunch. Has the best performance for a WSGI server, but lacks some quality of life features like worker concurrency.
* [Gunicorn](https://github.com/benoitc/gunicorn): A community favourite for a long time, of the three servers tested is the worst by far, but still one of the best options for a reliable WSGI server.
* [Uvicorn](https://github.com/encode/uvicorn): The only ASGI server tested. By far the most reliable, fault tolerant and productive web server. Bjoern could serve individual petitions faster, but, on a general basis, uvicorn is capable of attending slightly more request per second.

## How to

First of all is recomended to deploy the server and the test to different machines. Results where calculeted by a t2.micro machine from AWS.

### Deploying servers

First of all, install bjoern dependencies (notice that library names and packet managers may vary between operating systems).
```
# apt-get install python2-dev libev-dev
```
Install python deps
```
$ pip install -r requirements.txt
```
Run any server:
```bash
$ python src/wsgi.py # Bjoern
$ gunicorn --bind 0.0.0.0:8000 --workers <n> src.wsgi:app # Gunicorn
$ uvicorn --host 0.0.0.0 --port 8000 --workers <n> src.wsgi:app # Uvicorn
```

### Testing servers

Install locust and run with the provided locustfile
```
$ pip install locust
$ locust -f locustfile.py
```

Visit http://localhost:8089 and have fun.
