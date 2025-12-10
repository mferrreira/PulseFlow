from engine_app.ext.database import db
from engine_app.models.log import Log

def log_action(payload):
    log = Log(event=payload["event"], action="log_action", payload=str(payload))
    db.session.add(log)
    db.session.commit()

def send_email(payload):
    print("Email fake enviado:", payload)

def send_telegram_message(payload):
    log_action(payload)
    print("ENVIANDO MENSAGEM NO TELEGRAM")


def init_app(app):
    engine = app.extensions["engine"]
    engine.register_action("log_action", log_action)
    engine.register_action("send_email", send_email)
