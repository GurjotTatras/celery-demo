import os
import time
from celery import Celery
from utils import isprime

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x + y

@celery.task(name='tasks.multiply')
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x * y

@celery.task(name='tasks.prime_number')
def add(x: int) -> int:
    try:
        x = int(x)
    except:
        return False
    time.sleep(5)
    return isprime(x)