from celery import Celery

app = Celery('task')
app.config_from_object('celeryconfig')

@app.task
def sub_numbers(a, b):
    return a - b