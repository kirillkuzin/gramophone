from typing import List

from fastapi import FastAPI, Body

from gramophone import utils, config

app = FastAPI()


@app.post(config.SEND_MESSAGE_ENDPOINT)
async def send_messages_handler(telegram_ids: List[int] = Body(...),
                                message: str = Body(...)):
    await utils.aggregate_request(telegram_ids, message)
    return "ok"
