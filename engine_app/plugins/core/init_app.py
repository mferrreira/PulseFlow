from engine_app.plugins.core import actions, triggers


def init_app(app):
    actions.init_app(app)
    triggers.init_app(app)
