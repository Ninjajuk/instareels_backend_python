from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

# Enable CORS manually
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

# Initialize Instaloader
L = instaloader.Instaloader()

@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Instagram URL is required'}), 400

    try:
        # Extract shortcode from the URL
        if "/reel/" in url:
            shortcode = url.split("/reel/")[1].split("/")[0]
        elif "/p/" in url:
            shortcode = url.split("/p/")[1].split("/")[0]
        else:
            return jsonify({'error': 'Invalid Instagram URL'}), 400

        # Fetch post metadata
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # Check if the post contains a video
        if not post.is_video:
            return jsonify({'error': 'The provided URL does not contain a video'}), 400

        # Get the video URL
        video_url = post.video_url

        # Return the video URL for download
        return jsonify({'downloadLink': video_url})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to download the video'}), 500


# Endpoint to download Instagram stories by username
@app.route('/download/stories', methods=['GET'])
def download_stories():
    username = request.args.get('username')

    if not username:
        return jsonify({'error': 'Instagram username is required'}), 400

    try:
        # Fetch profile metadata
        profile = instaloader.Profile.from_username(L.context, username)

        # Get stories
        stories = []
        for story in L.get_stories([profile.userid]):
            for item in story.get_items():
                if item.is_video:
                    stories.append({'url': item.video_url, 'type': 'video'})
                else:
                    stories.append({'url': item.url, 'type': 'image'})

        if not stories:
            return jsonify({'error': 'No stories found for this user'}), 404

        # Return the list of story URLs
        return jsonify({'stories': stories})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch stories'}), 500

# Endpoint to download Instagram profile picture (DP) by username
@app.route('/download/dp', methods=['GET'])
def download_dp():
    username = request.args.get('username')

    if not username:
        return jsonify({'error': 'Instagram username is required'}), 400

    try:
        # Fetch profile metadata
        profile = instaloader.Profile.from_username(L.context, username)

        # Get profile picture URL
        dp_url = profile.profile_pic_url

        if not dp_url:
            return jsonify({'error': 'No profile picture found for this user'}), 404

        # Return the profile picture URL
        return jsonify({'dpUrl': dp_url})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch profile picture'}), 500
if __name__ == '__main__':
    app.run(debug=True)