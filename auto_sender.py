import os
from telethon import TelegramClient
import schedule
import asyncio

# Чтение данных из переменных окружения
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

# Подключение к Telegram
client = TelegramClient('user_session', api_id, api_hash)

# Функция для отправки сообщения
async def send_message():
    chat_id = -1266771326  # ID чата
    message = ".отн сделать подарок"  # Текст сообщения
    await client.send_message(chat_id, message)
    print(f"Сообщение отправлено в {chat_id}: {message}")

# Настройка расписания
def job():
    with client:
        client.loop.run_until_complete(send_message())

schedule.every(6).minutes.do(job)  # Меняй интервал, если нужно

# Основной цикл
async def main():
    await client.start(phone_number)  # Логин через номер телефона
    print("Автоматизация запущена!")
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)  # Асинхронный sleep вместо time.sleep(1)

with client:
    client.loop.run_until_complete(main())
