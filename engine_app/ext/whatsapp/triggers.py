class WhatsAppTrigger:
    key = "user.whatsapp.send_message"

    @staticmethod
    def handle(data):
        print("Trigger: mensagem enviada via whatsapp:", data)


def init_app(app):
    engine = app.extensions["engine"]
    engine.register_trigger(WhatsAppTrigger)
