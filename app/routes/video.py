from flask import Blueprint, request, jsonify
import instaloader
from app.utils.helpers import extract_shortcode

bp = Blueprint('video', __name__)
L = instaloader.Instaloader()

@bp.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Instagram URL is required'}), 400

    try:
        shortcode = extract_shortcode(url)
        if not shortcode:
            return jsonify({'error': 'Invalid Instagram URL'}), 400

        post = instaloader.Post.from_shortcode(L.context, shortcode)

        if not post.is_video:
            return jsonify({'error': 'The provided URL does not contain a video'}), 400

        return jsonify({'downloadLink': post.video_url})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to download the video'}), 500
