from flask import Blueprint, render_template, request, redirect, url_for
from engine_app.models.rule import Rule
from engine_app.models.log import Log
from engine_app.ext.database import db
from engine_app.ext.events import event_bus

webui_bp = Blueprint(
    "webui",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@webui_bp.get("/")
def home():
    rules = Rule.query.all()
    return render_template("webui/rules.html", rules=rules)

@webui_bp.get("/rules/new")
def new_rule():
    return render_template("webui/new_rule.html")

@webui_bp.post("/rules/new")
def create_rule():
    event = request.form["event"]
    action = request.form["action"]
    rule = Rule(event=event, action=action)
    db.session.add(rule)
    db.session.commit()
    return redirect(url_for("webui.home"))

@webui_bp.get("/simulate")
def simulate_page():
    return render_template("webui/simulate.html")

@webui_bp.post("/simulate")
def simulate_submit():
    event = request.form["event"]
    payload = {"info": request.form["payload"] or ""}
    event_bus.publish(event, payload)
    return redirect(url_for("webui.simulate_page"))

@webui_bp.get("/logs")
def logs_page():
    logs = Log.query.order_by(Log.timestamp.desc()).all()
    return render_template("webui/logs.html", logs=logs)


def init_app(app):
    app.register_blueprint(webui_bp, url_prefix="/")