# Hot reloading example

## Getting Started

To run a development environment, simply run:

```
docker-compose up
```

- The ExpressJS Node server is running at :3000
- The Kitura Swift server is running at :3100
- Java server to come.

## Production

To run a production environment, overlay `production.yml` on the `docker-compose.yml` file:

```
docker-compose -f docker-compose.yml -f production.yml up
```

This will additionally run a Zipkin server and also nginx load balancer.

## Configuration

Any shared variables to be used can be stored in the `.env` file.