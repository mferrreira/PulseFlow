from flask import Flask
from engine_app.ext import configuration, database, events, engine
from engine_app.ext.whatsapp import whatsapp
from engine_app.ext.telegram import telegram
from engine_app.plugins import core
from engine_app.blueprints.rules import rules_bp
from engine_app.blueprints.simulate import simulate_bp
from engine_app.blueprints.logs import logs_bp
from engine_app.webui import webui

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    configuration.init_app(app)
    database.init_app(app)
    events.init_app(app)
    engine.init_app(app)
    core.init_app(app)
    rules_bp.init_app(app)
    simulate_bp.init_app(app)
    logs_bp.init_app(app)
    whatsapp.init_app(app)
    telegram.init_app(app)
    webui.init_app(app)

    return app
