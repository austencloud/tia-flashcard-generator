from reportlab.lib.units import inch
from reportlab.lib import colors

class TitlePageGenerator:
    """Generates a title page for the flashcards PDF."""
    
    def __init__(self, canvas, page_width, page_height, resource_manager, card_renderer):
        self.canvas = canvas
        self.page_width = page_width
        self.page_height = page_height
        self.resource_manager = resource_manager
        self.card_renderer = card_renderer
    
    def create_title_page(self):
        """Create a beautiful title page with the logo."""
        # Draw a gradient background for the entire page
        self.card_renderer.draw_gradient_background(
            0, 0, 
            self.page_width, self.page_height,
            colors.Color(0.95, 0.95, 1),  # Light blue-gray
            colors.Color(1, 1, 1),        # White
            steps=20
        )
        
        # Draw subtle pattern on the title page
        self.card_renderer.draw_subtle_pattern(
            50, 50, 
            self.page_width-100, self.page_height-100, 
            colors.Color(0.5, 0.5, 0.8, 0.05)
        )
        
        # Place the logo in the center upper portion of the page
        cached_logo = self.resource_manager.get_logo()
        if cached_logo is not False:
            logo_width = 4 * inch
            logo_height = 4 * inch
            
            # Center the logo horizontally
            logo_x = (self.page_width - logo_width) / 2
            logo_y = self.page_height - 3 * inch - logo_height
            
            try:
                self.canvas.drawImage(cached_logo, logo_x, logo_y, width=logo_width, height=logo_height, mask='auto')
            except Exception:
                # Fallback if there's an issue drawing the image
                self.canvas.setFont("DejaVuSans-Bold", 30)
                self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
                text = "THE INSECT ASYLUM"
                text_width = self.canvas.stringWidth(text, "DejaVuSans-Bold", 30)
                self.canvas.drawString((self.page_width - text_width) / 2, logo_y + logo_height/2, text)
            
            # Draw a decorative line under the logo
            self.canvas.setStrokeColor(colors.Color(0.5, 0.5, 0.7))
            self.canvas.setLineWidth(2)
            self.canvas.line(logo_x, logo_y - 20, logo_x + logo_width, logo_y - 20)
            
            # Add title text
            self.canvas.setFont("DejaVuSans-Bold", 24)
            self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
            title = "Nature Exploration Flashcards"
            title_width = self.canvas.stringWidth(title, "DejaVuSans-Bold", 24)
            self.canvas.drawString((self.page_width - title_width) / 2, logo_y - 60, title)
            
            # Add subtitle
            self.canvas.setFont("DejaVuSans", 16)
            self.canvas.setFillColor(colors.Color(0.4, 0.4, 0.6))
            subtitle = "The Insect Asylum Collection"
            subtitle_width = self.canvas.stringWidth(subtitle, "DejaVuSans", 16)
            self.canvas.drawString((self.page_width - subtitle_width) / 2, logo_y - 90, subtitle)
