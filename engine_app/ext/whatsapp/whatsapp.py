from engine_app.ext.whatsapp import actions, triggers
from engine_app.ext.whatsapp.service import whatsapp_service

def init_app(app):
    if not hasattr(app, "extensions"):
        app.extensions = {}

    app.extensions["whatsapp_service"] = whatsapp_service

    actions.init_app(app)
    triggers.init_app(app)
