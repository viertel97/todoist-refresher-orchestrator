import telegram
from quarter_lib.akeyless import get_secrets
from quarter_lib.logging import setup_logging

logger = setup_logging(__name__)

TELEGRAM_TOKEN, CHAT_ID = get_secrets(["telegram/token", "telegram/chat_id"])


async def send_to_telegram(msg):
    await telegram.Bot(TELEGRAM_TOKEN).sendMessage(chat_id=int(CHAT_ID), text=msg, disable_notification=True)
