from engine_app.ext.database import db

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(64), nullable=False)
    action = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"<Rule {self.event} -> {self.action}>"
