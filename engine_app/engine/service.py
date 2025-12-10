from typing import Any, Callable, Dict, Iterable, Optional

from engine_app.models.rule import Rule


class EngineService:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self._actions: Dict[str, Callable[[Dict[str, Any]], None]] = {}
        self._triggers: Dict[str, Callable[[Dict[str, Any]], None]] = {}

    def register_action(self, key: str, handler: Callable[[Dict[str, Any]], None]) -> None:
        self._actions[key] = handler

    def register_actions(self, items: Dict[str, Callable[[Dict[str, Any]], None]]) -> None:
        for key, handler in items.items():
            self.register_action(key, handler)

    def register_trigger(self, trigger: Any) -> None:
        trigger_key = getattr(trigger, "key", None)
        if not trigger_key:
            raise ValueError("Trigger must define a `key` attribute.")

        handle_fn = getattr(trigger, "handle", None)
        if handle_fn is not None and not callable(handle_fn):
            raise ValueError("Trigger.handle must be callable when provided.")

        if trigger_key in self._triggers:
            return

        self._triggers[trigger_key] = handle_fn
        self.event_bus.subscribe(
            trigger_key,
            lambda data, ev=trigger_key, handler=handle_fn: self._handle_trigger(ev, data, handler),
        )

    def register_triggers(self, triggers: Iterable[Any]) -> None:
        for trigger in triggers:
            self.register_trigger(trigger)

    def _handle_trigger(
        self,
        event_name: str,
        data: Optional[Dict[str, Any]],
        trigger_callback: Optional[Callable[[Dict[str, Any]], None]],
    ) -> None:
        if trigger_callback:
            trigger_callback(data or {})
        self._process_event(event_name, data or {})

    def _process_event(self, event_name: str, data: Dict[str, Any]) -> None:
        rules = Rule.query.filter_by(event=event_name).all()

        print("[ENGINE]: Regras disponíveis:")
        for rule in rules:
            action_fn = self._actions.get(rule.action)
            print(f"{rule}:{action_fn}")
            if action_fn:
                payload = {"event": event_name, "data": data}
                action_fn(payload)
