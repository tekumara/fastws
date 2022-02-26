import time

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from starlette.concurrency import run_in_threadpool

app = FastAPI()


def send_email(message: str) -> None:
    time.sleep(2)
    print(f"sent {message}")


@app.websocket("/ws/send-notification/{domain}")
async def websocket_endpoint(websocket: WebSocket, domain: str) -> None:
    await websocket.accept()
    while True:
        try:
            username = await websocket.receive_text()

            email = f"{username.strip()}@{domain}"

            await websocket.send_json({"message": f"Sending email to {email}"})

            message = f"hi {email}!\n"
            await run_in_threadpool(send_email, message)

            await websocket.send_json({"message": f"Message sent to {email}"})

        except WebSocketDisconnect:
            pass
