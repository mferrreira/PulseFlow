from engine_app.ext.telegram import actions, triggers
from engine_app.ext.telegram.service import telegram_service

def init_app(app):
    if not hasattr(app, "extensions"):
        app.extensions = {}
    
    app.extensions["telegram_service"] = telegram_service

    actions.init_app(app)
    triggers.init_app(app)