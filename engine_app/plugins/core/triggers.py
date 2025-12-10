class UserRegisteredTrigger:
    key = "user.registered"

    @staticmethod
    def handle(data):
        print("Trigger: usuário registrado:", data)

class TaskCreatedTrigger:
    key = "task.created"

    @staticmethod
    def handle(data):
        print("Trigger: task criada:", data)

class TelegramMessageTrigger:
    key = "user.telegram.send_message"

    @staticmethod
    def handle(data):
        print("Trigger: mensagem enviada via telegram: ", data)

def init_app(app):
    engine = app.extensions["engine"]
    engine.register_trigger(UserRegisteredTrigger)
    engine.register_trigger(TaskCreatedTrigger)
    engine.register_trigger(TelegramMessageTrigger)
