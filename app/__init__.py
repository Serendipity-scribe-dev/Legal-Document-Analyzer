# app/__init__.py
from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from app.routes.ipc_routes import ipc_bp
    from app.routes.summarizer_routes import summarizer_bp

    app.register_blueprint(ipc_bp)
    app.register_blueprint(summarizer_bp)

    return app
