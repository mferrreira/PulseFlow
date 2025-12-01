from engine_app.models.log import Log
from engine_app.ext.database import db

def log_action(payload):
    log = Log(event=payload["event"], action="log_action", payload=str(payload))
    db.session.add(log)
    db.session.commit()

def send_email(payload):
    print("Email fake enviado:", payload)

def send_message(payload):
    log_action(payload)
    print("enviando mensagem...")

AVAILABLE_ACTIONS = {
    "log_action": log_action,
    "send_email": send_email,
    "send_message": send_message,
}
