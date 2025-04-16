# Celery fastapi program scaffold

## Components

There are four components in this service.
- REST Server
- Redis Broker
- Celery Worker
- Flower Server

### Redis Broker

Redis is an in-memory data store that can be used as a message broker in Celery, providing a simple and efficient way to manage task queues, making it an ideal choice for our solution.It receives tasks from the FastAPI service and places them in the queue for processing.

### Celery Worker

Consume tasks from the Redis queue and execute them asynchronously, then return the result to the Redis broker.

### Flower Server
It monitors the Celery cluster in real-time, offering a web-based interface to track task execution, worker performance, and queue status.

