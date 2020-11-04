from datetime import timedelta

from celery import Celery

import config

celery_app = Celery("worker", broker=config.BROKER)

celery_app.conf.task_routes = {"celery_worker.get_price": "test-queue"}

celery_app.conf.update(task_track_started=True)

celery_app.conf.beat_schedule = {
    "my-task": {"task": "celery_worker.get_price", "schedule": timedelta(minutes=config.TASK_TIME_MINUTES)}
}
