# gramophone

gramophone is a asynchronous microservice for sending messages to a group of users from the telegram bot's.

## Setup

gramophone is configured using environment variables:

- BOT_TOKEN - a token of your bot
- SEND_MESSAGE_ENDPOINT - endpoint for accepting requests to send messages (default is "/")

## Usage

For launch execute this:
```shell script
uvicorn gramophone.main:app --some options
```

Send a POST request to the gramophone with body:
```json
{
    "telegram_ids": [1, 2, 3, 4, 5],
    "message": "👋Hi all !\n🎉This is a test message !\n🙈By !"
}
```

## Requirements
- [fastapi](https://github.com/tiangolo/fastapi)
- [uvicorn](https://www.uvicorn.org)
- [httpx](https://github.com/encode/httpx)
