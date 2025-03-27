from reportlab.lib import colors
from reportlab.lib.units import inch


class StyleManager:
    """Manages styles and colors for the flashcards."""

    def __init__(self):
        self.card_width = 3.5 * inch
        self.card_height = 2 * inch
        self.header_height = 0.5 * inch
        self.category_colors = self._init_category_colors()
        self.typography = self._init_typography()

    def _init_typography(self):
        """Initialize typography settings for all categories."""
        return {
            "Nature Detectives": {
                "header_font": "DejaVuSans-Bold",
                "header_size": 14,
                "question_font": "DejaVuSans-Oblique",  # Italic style for curious detectives
                "question_size": 13,
            },
            "Animal Treasures": {
                "header_font": "DejaVuSerif-Bold",  # Serif for classic, museum feel
                "header_size": 14,
                "question_font": "DejaVuSerif",
                "question_size": 13,
            },
            "Nature's Art": {
                "header_font": "DejaVuSans-BoldOblique",  # Dynamic, artistic style
                "header_size": 14,
                "question_font": "DejaVuSans",
                "question_size": 13,
            },
            "Super Senses": {
                "header_font": "DejaVuSans-Bold",
                "header_size": 15,  # Slightly larger for emphasis
                "question_font": "DejaVuSans",
                "question_size": 13,
            },
            "Mystery Box": {
                "header_font": "DejaVuSansMono-Bold",  # Monospace for mystery/code feel
                "header_size": 14,
                "question_font": "DejaVuSansMono",
                "question_size": 12,  # Slightly smaller for more "coded" look
            },
            "Wild Homes": {
                "header_font": "DejaVuSerif-Bold",
                "header_size": 14,
                "question_font": "DejaVuSerif",
                "question_size": 13,
            },
            "Time Machine": {
                "header_font": "DejaVuSerif-Bold",  # Classic, old-time feel
                "header_size": 14,
                "question_font": "DejaVuSerif",
                "question_size": 13,
            },
            "Texture Explorers": {
                "header_font": "DejaVuSans-Bold",
                "header_size": 14,
                "question_font": "DejaVuSans-Oblique",  # Italic for dynamic feeling
                "question_size": 13,
            },
            "Compare & Contrast": {
                "header_font": "DejaVuSansMono-Bold",  # Technical feel
                "header_size": 13,  # Slightly smaller for longer category name
                "question_font": "DejaVuSansMono",
                "question_size": 12,
            },
            "Nature's Helpers": {
                "header_font": "DejaVuSans-Bold",
                "header_size": 14,
                "question_font": "DejaVuSans",
                "question_size": 13,
            },
            "Nature's Puzzles": {
                "header_font": "DejaVuSansMono-Bold",  # Code-like for puzzles
                "header_size": 14,
                "question_font": "DejaVuSansMono",
                "question_size": 12,
            },
            "Imagination Station": {
                "header_font": "DejaVuSans-BoldOblique",  # Dynamic, creative style
                "header_size": 14,
                "question_font": "DejaVuSans-Oblique",
                "question_size": 13,
            },
        }

    def get_default_typography(self):
        """Return default typography settings."""
        return {
            "header_font": "DejaVuSans-Bold",
            "header_size": 14,
            "question_font": "DejaVuSans",
            "question_size": 13,
        }

    def get_typography(self, category):
        """Get typography settings for a category."""
        return self.typography.get(category, self.get_default_typography())

    def _init_category_colors(self):
        """Initialize color schemes for all categories."""
        return {
            # Original categories with renamed versions
            "Nature Detectives": {
                "header": colors.Color(1, 0.9, 0.2),
                "gradient_start": colors.Color(1, 0.95, 0.5),
                "gradient_end": colors.Color(1, 1, 0.8),
                "text_color": colors.Color(0.6, 0.3, 0),
                "border_color": colors.Color(0.9, 0.7, 0.0),
                "shadow_color": colors.Color(0.9, 0.7, 0.0, 0.3),
                "pattern_color": colors.Color(0.95, 0.8, 0.2, 0.1),
            },
            "Animal Treasures": {
                "header": colors.Color(1, 0.6, 0.6),
                "gradient_start": colors.Color(1, 0.7, 0.7),
                "gradient_end": colors.Color(1, 0.9, 0.8),
                "text_color": colors.Color(0.7, 0.2, 0.3),
                "border_color": colors.Color(0.8, 0.3, 0.3),
                "shadow_color": colors.Color(0.8, 0.3, 0.3, 0.3),
                "pattern_color": colors.Color(0.9, 0.5, 0.5, 0.1),
            },
            "Nature's Art": {
                "header": colors.Color(0.4, 0.8, 0.4),
                "gradient_start": colors.Color(0.6, 0.9, 0.6),
                "gradient_end": colors.Color(0.8, 1, 0.8),
                "text_color": colors.Color(0, 0.5, 0.2),
                "border_color": colors.Color(0.2, 0.6, 0.2),
                "shadow_color": colors.Color(0.2, 0.6, 0.2, 0.3),
                "pattern_color": colors.Color(0.3, 0.7, 0.3, 0.1),
            },
            "Super Senses": {
                "header": colors.Color(0.4, 0.8, 0.8),
                "gradient_start": colors.Color(0.5, 0.8, 0.9),
                "gradient_end": colors.Color(0.8, 0.95, 1),
                "text_color": colors.Color(0, 0.3, 0.6),
                "border_color": colors.Color(0.0, 0.5, 0.7),
                "shadow_color": colors.Color(0.0, 0.5, 0.7, 0.3),
                "pattern_color": colors.Color(0.3, 0.7, 0.9, 0.1),
            },
            "Mystery Box": {
                "header": colors.Color(0.7, 0.6, 0.9),
                "gradient_start": colors.Color(0.7, 0.6, 0.9),
                "gradient_end": colors.Color(0.9, 0.85, 1),
                "text_color": colors.Color(0.4, 0, 0.6),
                "border_color": colors.Color(0.5, 0.3, 0.7),
                "shadow_color": colors.Color(0.5, 0.3, 0.7, 0.3),
                "pattern_color": colors.Color(0.6, 0.5, 0.8, 0.1),
            },
            "Wild Homes": {
                "header": colors.Color(1, 0.5, 0.5),
                "gradient_start": colors.Color(1, 0.6, 0.5),
                "gradient_end": colors.Color(1, 0.8, 0.7),
                "text_color": colors.Color(0.8, 0.2, 0),
                "border_color": colors.Color(0.8, 0.4, 0.2),
                "shadow_color": colors.Color(0.8, 0.4, 0.2, 0.3),
                "pattern_color": colors.Color(0.9, 0.5, 0.3, 0.1),
            },
            # New categories with new color schemes
            "Time Machine": {
                "header": colors.Color(0.6, 0.4, 0.8),
                "gradient_start": colors.Color(0.7, 0.5, 0.9),
                "gradient_end": colors.Color(0.9, 0.8, 1),
                "text_color": colors.Color(0.4, 0.1, 0.5),
                "border_color": colors.Color(0.5, 0.3, 0.6),
                "shadow_color": colors.Color(0.5, 0.3, 0.6, 0.3),
                "pattern_color": colors.Color(0.7, 0.6, 0.9, 0.1),
            },
            "Texture Explorers": {
                "header": colors.Color(0.8, 0.5, 0.2),
                "gradient_start": colors.Color(0.9, 0.6, 0.3),
                "gradient_end": colors.Color(1, 0.8, 0.6),
                "text_color": colors.Color(0.6, 0.3, 0.1),
                "border_color": colors.Color(0.7, 0.4, 0.1),
                "shadow_color": colors.Color(0.7, 0.4, 0.1, 0.3),
                "pattern_color": colors.Color(0.9, 0.7, 0.4, 0.1),
            },
            "Compare & Contrast": {
                "header": colors.Color(0.2, 0.6, 0.8),
                "gradient_start": colors.Color(0.3, 0.7, 0.9),
                "gradient_end": colors.Color(0.6, 0.9, 1),
                "text_color": colors.Color(0.1, 0.4, 0.6),
                "border_color": colors.Color(0.1, 0.5, 0.7),
                "shadow_color": colors.Color(0.1, 0.5, 0.7, 0.3),
                "pattern_color": colors.Color(0.4, 0.7, 0.9, 0.1),
            },
            "Nature's Helpers": {
                "header": colors.Color(0.3, 0.7, 0.3),
                "gradient_start": colors.Color(0.4, 0.8, 0.4),
                "gradient_end": colors.Color(0.7, 1, 0.7),
                "text_color": colors.Color(0.1, 0.5, 0.1),
                "border_color": colors.Color(0.2, 0.6, 0.2),
                "shadow_color": colors.Color(0.2, 0.6, 0.2, 0.3),
                "pattern_color": colors.Color(0.5, 0.8, 0.5, 0.1),
            },
            "Nature's Puzzles": {
                "header": colors.Color(0.9, 0.4, 0.7),
                "gradient_start": colors.Color(0.95, 0.5, 0.8),
                "gradient_end": colors.Color(1, 0.8, 0.9),
                "text_color": colors.Color(0.6, 0.2, 0.4),
                "border_color": colors.Color(0.7, 0.3, 0.5),
                "shadow_color": colors.Color(0.7, 0.3, 0.5, 0.3),
                "pattern_color": colors.Color(0.9, 0.6, 0.8, 0.1),
            },
            "Imagination Station": {
                "header": colors.Color(0.95, 0.7, 0.2),
                "gradient_start": colors.Color(0.98, 0.8, 0.3),
                "gradient_end": colors.Color(1, 0.9, 0.6),
                "text_color": colors.Color(0.7, 0.4, 0),
                "border_color": colors.Color(0.8, 0.5, 0),
                "shadow_color": colors.Color(0.8, 0.5, 0, 0.3),
                "pattern_color": colors.Color(0.95, 0.85, 0.4, 0.1),
            },
        }

    def get_default_color_scheme(self):
        """Return a default color scheme for categories without defined styles."""
        return {
            "header": colors.lightgrey,
            "gradient_start": colors.whitesmoke,
            "gradient_end": colors.white,
            "text_color": colors.navy,
            "border_color": colors.navy,
            "shadow_color": colors.Color(0, 0, 0, 0.2),
            "pattern_color": colors.Color(0, 0, 0, 0.1),
        }

    def get_color_scheme(self, category):
        """Get the color scheme for a category."""
        return self.category_colors.get(category, self.get_default_color_scheme())
