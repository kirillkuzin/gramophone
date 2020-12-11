import asyncio
from typing import List

import httpx

from gramophone import config


async def aggregate_request(telegram_ids: List[int], message: str):
    send_message_url = f'{config.TELEGRAM_SEND_MESSAGE_URL}?text={message}'

    async with httpx.AsyncClient() as http_client:
        for telegram_id in telegram_ids:
            tasks = list()
            tasks.append(asyncio.create_task(send_message(telegram_id,
                                                          send_message_url,
                                                          http_client)))

        await asyncio.gather(*tasks)


async def send_message(telegram_id: int,
                       send_message_url: str,
                       http_client: httpx.AsyncClient):
    send_message_url = f'{send_message_url}&chat_id={telegram_id}'

    await http_client.get(send_message_url)
