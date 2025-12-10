import os
import threading

from telebot import TeleBot
from telebot.apihelper import ApiException, ApiTelegramException

class TelegramService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls)
            instance._bot = TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
            instance._polling_started = False
            cls._instance = instance
        return cls._instance

    def __init__(self):
        if self._polling_started:
            return

        if os.environ.get("FLASK_ENV") == "development":
            if os.environ.get("WERKZEUG_RUN_MAIN") not in ("true", "1", "True"):
                return

        thread = threading.Thread(
            target=lambda: self._bot.polling(non_stop=True, skip_pending=True),
            daemon=True,
        )
        thread.start()
        self._polling_started = True

    def send_message(self, number: str, message: str):
        try: 
            print("[TELEGRAM SERVICE]: Enviando mensagem:\n")

            self._bot.send_message(chat_id=number, text=message)
            TeleBot.send_message()
        except ApiTelegramException or ApiException or TypeError as e:
            print(f"Ocorreu um erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")



telegram_service = TelegramService()
