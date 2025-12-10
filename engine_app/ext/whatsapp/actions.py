from engine_app.plugins.core.actions import log_action
from engine_app.ext.whatsapp.service import whatsapp_service

def send_whatsapp_message(payload):
    log_action(payload)
    info = payload.get("data", {}).get("info", {})
    message = info.get("message", "")
    number = info.get("number", "")
    whatsapp_service.send_message(number, message)

def init_app(app):
    engine = app.extensions["engine"]
    engine.register_action("send_whatsapp_message", send_whatsapp_message)
