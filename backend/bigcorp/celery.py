import os

from celery import Celery

# from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigcorp.settings")
app = Celery("bigcorp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'multiply-task-crontab': {
#         'task': 'multiply_two_numbers',
#         'schedule': crontab(hour=7, minute=30, day_of_week=1),
#         'args': (16, 16),
#     },
#     'multiply-every-5-seconds': {
#         'task': 'multiply_two_numbers',
#         'schedule': 5.0,
#         'args': (16, 16)
#     },
#     'add-every-30-seconds': {
#         'task': 'movies.tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }