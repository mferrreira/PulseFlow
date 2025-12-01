from engine_app.models.rule import Rule
from engine_app.services.engine.triggers import AVAILABLE_TRIGGERS
from engine_app.services.engine.actions import AVAILABLE_ACTIONS

def process_event(event_name, data):
    rules = Rule.query.filter_by(event=event_name).all()

    print("[ENGINE]: Regras disponíveis:")
    for rule in rules:
        action_fn = AVAILABLE_ACTIONS.get(rule.action)
        print(f"{rule}:{action_fn}")
        if action_fn:
            payload = {"event": event_name, "data": data}
            action_fn(payload)

def register_engine(event_bus):
    print(f"[ENGINGE]: Eventos disponível: ")
    for event_name in AVAILABLE_TRIGGERS:
        print(event_name)
        event_bus.subscribe(event_name, lambda data, ev=event_name: process_event(ev, data))
    
