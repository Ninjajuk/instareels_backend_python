from app import create_app
import os
port = int(os.environ.get("PORT", 5000))  # Use PORT provided by Render or default to 5000
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
    




