from flask import Blueprint, jsonify
from engine_app.models.log import Log

logs_bp = Blueprint("logs", __name__)

@logs_bp.get("/")
def list_logs():
    logs = Log.query.all()
    return jsonify([
        {
            "id": log.id,
            "event": log.event,
            "action": log.action,
            "timestamp": log.timestamp.isoformat(),
            "payload": log.payload
        }
        for log in logs
    ])


def init_app(app):
    app.register_blueprint(logs_bp, url_prefix="/logs")