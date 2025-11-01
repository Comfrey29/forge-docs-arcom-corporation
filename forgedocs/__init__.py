from flask import Flask
import os

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, '../templates')  # ajusta si cal segons la teva estructura

    app = Flask(__name__, template_folder=template_dir)
    from .routes import main
    app.register_blueprint(main)
    return app
