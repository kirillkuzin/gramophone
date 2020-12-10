from typing import List
import asyncio

import httpx
from fastapi import FastAPI, Body

from gramophone import config

app = FastAPI()


async def send_messages(telegram_id: int,
                        send_message_url: str,
                        http_client: httpx.AsyncClient):
    send_message_url = f'{send_message_url}&chat_id={telegram_id}'

    response = await http_client.get(send_message_url)


@app.post(config.SEND_MESSAGE_ENDPOINT)
async def send_messages_handler(telegram_ids: List[int] = Body(...),
                                message: str = Body(...)):
    send_text = f'{config.TELEGRAM_SEND_MESSAGE_URL}?text={message}'

    async with httpx.AsyncClient() as client:
        for telegram_id in telegram_ids:
            tasks = list()
            tasks.append(asyncio.create_task(send_messages(telegram_id,
                                                           send_text,
                                                           client)))

        await asyncio.gather(*tasks)

    return "ok"
