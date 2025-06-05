python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python run.py


insta_downloader_api/
│
├── app/
│   ├── __init__.py              # Initializes the Flask app
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── video.py             # /download route logic
│   │   ├── stories.py           # /download/stories route logic
│   │   └── dp.py                # /download/dp route logic
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py           # Common helper functions (e.g., extract shortcode)
│   └── config.py                # Configuration file (if needed)
│
├── run.py                       # Entry point to run the server
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview

