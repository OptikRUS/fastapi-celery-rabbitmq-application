Deploy RabbitMQ: `docker-compose up --build -d`

Run celery worker: `celery -A main.celery worker --loglevel=info -Q universities,university`

Run flower: `celery -A main.celery flower --port=5555`

Run app: `uvicorn main:app --reload`

App Swagger UI: ` http://127.0.0.1:8000/docs`

Flower tasks: `http://127.0.0.1:5555/tasks`

RabbitMQ: `http://127.0.0.1:15672/`

Thanks by this [Guide](https://medium.com/cuddle-ai/async-architecture-with-fastapi-celery-and-rabbitmq-c7d029030377)