import os


BOT_TOKEN = os.getenv('BOT_TOKEN')

SEND_MESSAGE_ENDPOINT = os.getenv('SEND_MESSAGE_ENDPOINT', '/')

TELEGRAM_API_URL = 'https://api.telegram.org/bot'
TELEGRAM_SEND_MESSAGE_URL = f'{TELEGRAM_API_URL}{BOT_TOKEN}/sendMessage'
