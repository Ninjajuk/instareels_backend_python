# app/routes/status.py
from flask import Blueprint, jsonify

bp = Blueprint('status', __name__)

@bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': '📡 API is live and running'}), 200

@bp.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'OK', 'service': 'Instagram Downloader API'}), 200
