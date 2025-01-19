from telethon import TelegramClient
import schedule
import time

# Введи свои данные
api_id = 26071362  # Твой API ID с my.telegram.org
api_hash = "c3d12bc02851cde9de371fa1a919bd76"  # Твой API Hash с my.telegram.org
phone_number = "+77712388254"  # Твой номер телефона в формате +123456789

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
        time.sleep(1)

with client:
    client.loop.run_until_complete(main())
