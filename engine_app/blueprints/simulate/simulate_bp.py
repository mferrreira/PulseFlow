from flask import Blueprint, request
from engine_app.ext.events import event_bus

simulate_bp = Blueprint("simulate", __name__)

@simulate_bp.post("/event")
def simulate_event():
    payload = request.json
    event_bus.publish(payload["event"], payload.get("data"))
    return {"message": "event dispatched"}

def init_app(app):
    app.register_blueprint(simulate_bp, url_prefix="/simulate")