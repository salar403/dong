import telegram
from celery import shared_task
from persiantools.jdatetime import JalaliDateTime

from backend.environments import BOT_TOKEN, CHAT_IDS, PLATFORM


@shared_task(queue="notifications")
def send_message(message: str, log_type: str):
    bot = telegram.Bot(token=BOT_TOKEN)
    try:
        message += f"\n {str(JalaliDateTime.now())}"
        bot.send_message(text=message, chat_id=CHAT_IDS[log_type])
    except Exception as error:
        raise error


@shared_task(queue="notifications")
def send_file(file: str, log_type: str, caption: str = None):
    bot = telegram.Bot(token=BOT_TOKEN)
    try:
        bot.sendDocument(
            chat_id=CHAT_IDS[log_type], document=open(file, "rb"), caption=caption
        )
    except Exception as error:
        raise error


@shared_task(queue="notifications")
def SendPhoto(file: str, log_type: str, caption: str = None):
    bot = telegram.Bot(token=BOT_TOKEN)
    try:
        bot.sendPhoto(
            chat_id=CHAT_IDS[log_type], photo=open(file, "rb"), caption=caption
        )
    except Exception as error:
        raise error


def simple_log(message: str, level: str):
    if PLATFORM != "ci/cd":
        send_message.apply_async(args=(message, level))
