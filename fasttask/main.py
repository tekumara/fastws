from starlette.concurrency import run_in_threadpool
from typing import Optional
import time
from fastapi import BackgroundTasks, Depends, FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


def write_log(message: str):
    time.sleep(10)
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}


@app.websocket("/ws/send-notification/{email}")
async def websocket_endpoint(websocket: WebSocket, email: str):
    await websocket.accept()
    while True:
        try:
            # Wait for any message from the client
            await websocket.receive_text()

            await websocket.send_json({"message": f"Sending email to {email}"})

            message = f"message to {email}\n"
            await run_in_threadpool(write_log, message)

            await websocket.send_json({"message": "Message sent"})

        except WebSocketDisconnect:
            pass
