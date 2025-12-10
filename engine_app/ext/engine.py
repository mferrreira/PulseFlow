from engine_app.ext.events import event_bus
from engine_app.engine.service import EngineService

engine_service = EngineService(event_bus)

def init_app(app):
    if not hasattr(app, "extensions"):
        app.extensions = {}

    app.extensions["engine"] = engine_service
