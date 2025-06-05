from .video import bp as video_bp
from .story import bp as stories_bp
from .dp import bp as dp_bp
from .status import bp as status_bp  

# List of all blueprints to register in the main app
__all__ = ['video_bp', 'stories_bp', 'dp_bp' , 'status_bp']
