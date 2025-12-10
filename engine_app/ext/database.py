from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)

    with app.app_context():
        from engine_app.services.populate_db_default import ensure_default_rules
        from engine_app.models.rule import Rule
        from engine_app.models.log import Log
        db.create_all()
        ensure_default_rules()
