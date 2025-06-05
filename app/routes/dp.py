from flask import Blueprint, request, jsonify
import instaloader

bp = Blueprint('dp', __name__)
L = instaloader.Instaloader()

@bp.route('/download/dp', methods=['GET'])
def download_dp():
    username = request.args.get('username')

    if not username:
        return jsonify({'error': 'Instagram username is required'}), 400

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        dp_url = profile.profile_pic_url

        if not dp_url:
            return jsonify({'error': 'No profile picture found for this user'}), 404

        return jsonify({'dpUrl': dp_url})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch profile picture'}), 500
