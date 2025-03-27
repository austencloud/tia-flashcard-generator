from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

class ResourceManager:
    """Handles resource loading and caching for the flashcard generator."""
    
    def __init__(self, logo_path="insect_asylum_logo.png"):
        self.logo_path = logo_path
        self.logo_cache = None
        self._register_fonts()
    
    def _register_fonts(self):
        """Register fonts needed for the flashcards."""
        # Base fonts
        pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))
        pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "DejaVuSans-Bold.ttf"))
        
        # Additional fonts - these would need to be available in your system
        # or distributed with your application
        pdfmetrics.registerFont(TTFont("DejaVuSerif", "DejaVuSerif.ttf"))
        pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", "DejaVuSerif-Bold.ttf"))
        pdfmetrics.registerFont(TTFont("DejaVuSans-Oblique", "DejaVuSans-Oblique.ttf"))
        pdfmetrics.registerFont(TTFont("DejaVuSans-BoldOblique", "DejaVuSans-BoldOblique.ttf"))
        pdfmetrics.registerFont(TTFont("DejaVuSansMono", "DejaVuSansMono.ttf"))
        pdfmetrics.registerFont(TTFont("DejaVuSansMono-Bold", "DejaVuSansMono-Bold.ttf"))


    
    def get_logo(self):
        """Cache and return the logo image."""
        if self.logo_cache is None:
            try:
                self.logo_cache = ImageReader(self.logo_path)
            except Exception as e:
                print(f"Warning: Could not load logo ({e})")
                self.logo_cache = False  # Use False to indicate a failed load attempt
        return self.logo_cache
