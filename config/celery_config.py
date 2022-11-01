import os
from functools import lru_cache
from kombu import Queue
from dotenv import load_dotenv

load_dotenv()


def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}


class BaseConfig:
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "rpc://")

    CELERY_TASK_QUEUES: list[Queue] = [
        # default queue
        Queue("celery"),
        # custom queue
        Queue("universities"),
        Queue("university"),
    ]

    CELERY_TASK_ROUTES = (route_task,)


class DevelopmentConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
    }
    config_name = os.getenv("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()

print(os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//"))
