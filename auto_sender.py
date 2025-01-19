from telethon import TelegramClient
import schedule
import time

# Введи свои данные
api_id = int("YOUR_API_ID")  # Твой API ID с my.telegram.org
api_hash = "YOUR_API_HASH"  # Твой API Hash с my.telegram.org
phone_number = "YOUR_PHONE_NUMBER"  # Твой номер телефона в формате +123456789

# Подключение к Telegram
client = TelegramClient('user_session', api_id, api_hash)

# Функция для отправки сообщения
async def send_message():
    chat_id = "CHAT_ID_OR_USERNAME"  # Укажи ID чата или @username
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
        time.sleep(1)

with client:
    client.loop.run_until_complete(main())
 
