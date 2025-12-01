def user_registered(data):
    print("Trigger: usuário registrado:", data)

def task_created(data):
    print("Trigger: task criada:", data)

def send_message(data):
    print("Trigger: mensagem enviada: ", data)

AVAILABLE_TRIGGERS = {
    "user.registered": user_registered,
    "task.created": task_created,
    "user.send_message": send_message,
}
