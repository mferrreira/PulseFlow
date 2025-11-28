class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_name, callback):
        self.subscribers.setdefault(event_name, []).append(callback)

    def publish(self, event_name, data):
        for callback in self.subscribers.get(event_name, []):
            callback(data)

event_bus = EventBus()

def init_app(app):
    from engine_app.services.engine.engine import register_engine
    register_engine(event_bus)
