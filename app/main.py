from datetime import timedelta
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from celery_worker import create_task
from celery.result import AsyncResult

app = FastAPI()


@app.post("/task/{x}")
async def run_task(x):
    amount = int(x)
    task = create_task.delay(amount)
    return JSONResponse({"task_id": task.id})

@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)