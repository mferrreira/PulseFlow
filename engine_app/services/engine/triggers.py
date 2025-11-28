def user_registered(data):
    print("Trigger: usuário registrado:", data)

def task_created(data):
    print("Trigger: task criada:", data)

AVAILABLE_TRIGGERS = {
    "user.registered": user_registered,
    "task.created": task_created,
}
