# Hot reloading example

## Getting Started

To run a development environment, simply run:

```
docker-compose up
```

- localhost:3000: ExpressJS Node server
- localhost:3100: Kitura Swift server
- localhost:3200: Flask Python server 

## Production

To run a production environment, overlay `production.yml` on the `docker-compose.yml` file:

```
docker-compose -f docker-compose.yml -f production.yml up
```

This will additionally run a Zipkin server and also nginx load balancer.

## Configuration

Any shared variables to be used can be stored in the `.env` file.