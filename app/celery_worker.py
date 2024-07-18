import os
import time

from celery import Celery
from dotenv import load_dotenv

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(bind=True, name="create_task")
def create_task(self,a):
    for i in range(10):
        self.update_state(state='PROGRESS', meta={'current': i, 'total': 10})
        time.sleep(a)
    return f"Slept for {a} seconds"