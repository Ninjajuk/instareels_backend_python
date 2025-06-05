from flask import Flask
from flask_cors import CORS
from .routes import video_bp, stories_bp, dp_bp , status_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import video, story, dp
    app.register_blueprint(video.bp)
    app.register_blueprint(story.bp)
    app.register_blueprint(dp.bp)
    app.register_blueprint(status_bp)  # 👈 Register status route

    return app
