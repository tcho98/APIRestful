from fastapi import FastAPI
from models import Task
from fastapi import Request

app = FastAPI()

@app.delete('/task/{pk}')
async def remove(pk: str):
    task = Task.get(pk)
    return task.delete(pk)


@app.put('/tasks/{pk}')
async def update(pk: str, request: Request):
    task = Task.get(pk)
    body = await request.json()
    task.complete = int(body['complete'])
    return task.save()


@app.post('/tasks')
async def create(task: Task):
    task.save()


@app.get("/tasks")
async def all():
    return[format(pk) for ok in Task.all_pks()]