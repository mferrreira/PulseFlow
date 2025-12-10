class TelegramTrigger:
    key = "user.telegram.send_message"

    @staticmethod
    def handle(data):
        print("[TELEGRAM][Trigger]: Mensagem enviada via Telegram: ", data)


def init_app(app):
    engine = app.extensions["engine"]
    engine.register_trigger(TelegramTrigger)