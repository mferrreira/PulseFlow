from flask_tailwind import Tailwind

tw = Tailwind()

def init_app(app):
    app.config['TAILWIND_INPUT'] = 'engine_app/webui/tailwind/src/input.css'
    app.config['TAILWIND_OUTPUT'] = 'engine_app/webui/static/css/tailwind.css'

    tw.init_app(app)
