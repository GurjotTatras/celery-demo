# Docker Flask Celery Redis

A basic [Docker Compose](https://docs.docker.com/compose/) template for orchestrating a [Flask](http://flask.pocoo.org/) application & a [Celery](http://www.celeryproject.org/) queue with [Redis](https://redis.io/)

### Installation

```bash
git clone https://github.com/GurjotTatras/celery-demo.git
```

### Build & Launch

```bash
docker-compose up -d --build
```

To add more workers:
```bash
docker-compose up -d --scale worker=5 --no-recreate
```
This will expose the Flask application's endpoints on port `5010` as well as a [Flower](https://github.com/mher/flower) server for monitoring workers on port `5558`

To shut down:

```bash
docker-compose down
```