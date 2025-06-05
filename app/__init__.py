from flask import Flask
from flask_cors import CORS
from .routes.video import bp as video_bp
from .routes.story import bp as stories_bp
from .routes.dp import bp as dp_bp
from .routes.status import bp as status_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(video_bp)
    app.register_blueprint(stories_bp)
    app.register_blueprint(dp_bp)
    app.register_blueprint(status_bp)

    return app
