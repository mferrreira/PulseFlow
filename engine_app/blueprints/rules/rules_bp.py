from flask import Blueprint, request, jsonify
from engine_app.ext.database import db
from engine_app.models.rule import Rule

rules_bp = Blueprint("rules", __name__)

@rules_bp.get("/")
def list_rules():
    rules = Rule.query.all()
    return jsonify([
        {"id": r.id, "event": r.event, "action": r.action}
        for r in rules
    ])

@rules_bp.post("/")
def create_rule():
    data = request.json
    rule = Rule(event=data["event"], action=data["action"])
    db.session.add(rule)
    db.session.commit()
    return {"message": "Rule created"}, 201

def init_app(app):
    app.register_blueprint(rules_bp, url_prefix="/rules")