from flask import Blueprint, request, jsonify
import instaloader

bp = Blueprint('stories', __name__)
L = instaloader.Instaloader()

@bp.route('/download/stories', methods=['GET'])
def download_stories():
    username = request.args.get('username')

    if not username:
        return jsonify({'error': 'Instagram username is required'}), 400

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        stories = []
        for story in L.get_stories([profile.userid]):
            for item in story.get_items():
                if item.is_video:
                    stories.append({'url': item.video_url, 'type': 'video'})
                else:
                    stories.append({'url': item.url, 'type': 'image'})

        if not stories:
            return jsonify({'error': 'No stories found for this user'}), 404

        return jsonify({'stories': stories})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch stories'}), 500
