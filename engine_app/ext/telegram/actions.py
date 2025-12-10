from engine_app.plugins.core.actions import log_action
from engine_app.ext.telegram.service import telegram_service

def send_telegram_message(payload):
    log_action(payload)
    info = payload.get("data", {}).get("info", {})
    message = info.get("message", "")
    number = info.get("number", "")

    telegram_service.send_message(number, message)

def init_app(app):
    engine = app.extensions["engine"]
    engine.register_action("send_telegram_message", send_telegram_message)