# Hot reloading example

## Getting Started

To run a development environment, simply run:

```
docker-compose up
```

- The ExpressJS Node server is running at localhost:3000
- The Kitura Swift server is running at localhost:3100
- The Flask Python server is running at localhost:3200

## Production

To run a production environment, overlay `production.yml` on the `docker-compose.yml` file:

```
docker-compose -f docker-compose.yml -f production.yml up
```

This will additionally run a Zipkin server and also nginx load balancer.

## Configuration

Any shared variables to be used can be stored in the `.env` file.