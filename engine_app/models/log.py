from engine_app.ext.database import db
from datetime import datetime

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(64))
    action = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    payload = db.Column(db.Text)
