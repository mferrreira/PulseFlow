from typing import List

from engine_app.ext.database import db
from engine_app.models.rule import Rule

DEFAULT_RULES: List[dict] = [
    {"event": "user.registered", "action": "log_action"},
    {"event": "user.registered", "action": "send_email"},
    {"event": "user.whatsapp.send_message", "action": "send_whatsapp_message"},
    {"event": "user.telegram.send_message", "action": "send_telegram_message"},
]

def ensure_default_rules():
    created = False

    for rule_data in DEFAULT_RULES:
        exists = Rule.query.filter_by(
            event=rule_data["event"],
            action=rule_data["action"],
        ).first()
        if exists:
            continue

        db.session.add(Rule(**rule_data))
        created = True

    if created:
        db.session.commit()
