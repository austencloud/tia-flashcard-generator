import random
from reportlab.lib.units import inch
from reportlab.lib import colors


class CardRenderer:
    """Renders card elements and components."""

    def __init__(self, canvas, style_manager, resource_manager):
        self.canvas = canvas
        self.style_manager = style_manager
        self.resource_manager = resource_manager

    def draw_card_shadow(
        self, x, y, width, height, radius=10, shadow_color=None, offset=3
    ):
        """Draw a shadow beneath the card to create a float effect."""
        if shadow_color is None:
            shadow_color = colors.Color(0, 0, 0, 0.2)

        self.canvas.saveState()
        self.canvas.setFillColor(shadow_color)
        self.canvas.roundRect(
            x + offset, y - offset, width, height, radius, fill=1, stroke=0
        )
        self.canvas.restoreState()

    def draw_text_with_shadow(
        self, text, x, y, font_name, font_size, main_color, shadow_color=None, offset=1
    ):
        """Draw text with a subtle shadow effect."""
        if shadow_color is None:
            shadow_color = colors.Color(0, 0, 0, 0.3)

        self.canvas.setFont(font_name, font_size)
        self.canvas.setFillColor(shadow_color)
        self.canvas.drawString(x + offset, y - offset, text)
        self.canvas.setFillColor(main_color)
        self.canvas.drawString(x, y, text)

    def draw_gradient_background(
        self, x, y, width, height, start_color, end_color, steps=15
    ):
        """Draw a vertical gradient background."""
        for i in range(steps):
            ratio = i / float(steps - 1)
            r = start_color.red + (end_color.red - start_color.red) * ratio
            g = start_color.green + (end_color.green - start_color.green) * ratio
            b = start_color.blue + (end_color.blue - start_color.blue) * ratio
            current_color = colors.Color(r, g, b)

            self.canvas.setFillColor(current_color)
            segment_height = height / steps
            self.canvas.rect(
                x, y + (i * segment_height), width, segment_height, fill=1, stroke=0
            )

    def draw_subtle_pattern(self, x, y, width, height, pattern_color):
        """Draw a subtle dot pattern background."""
        self.canvas.saveState()
        self.canvas.setFillColor(pattern_color)

        # Draw a grid of small dots
        spacing = 15
        dot_size = 1.5

        for i in range(int(width / spacing)):
            for j in range(int(height / spacing)):
                # Add some random offset for a more natural look
                offset_x = random.uniform(-2, 2)
                offset_y = random.uniform(-2, 2)

                dot_x = x + (i * spacing) + offset_x
                dot_y = y + (j * spacing) + offset_y

                # Only draw if within bounds
                if dot_x > x and dot_x < x + width and dot_y > y and dot_y < y + height:
                    self.canvas.circle(dot_x, dot_y, dot_size, fill=1, stroke=0)

        self.canvas.restoreState()

    def draw_corner_accents(self, x, y, width, height, color, size=8):
        """Draw simple corner accents."""
        self.canvas.setStrokeColor(color)
        self.canvas.setLineWidth(1.5)

        # Top-left corner
        self.canvas.line(x + 5, y + height - 5, x + 5 + size, y + height - 5)
        self.canvas.line(x + 5, y + height - 5, x + 5, y + height - 5 - size)

        # Top-right corner
        self.canvas.line(
            x + width - 5, y + height - 5, x + width - 5 - size, y + height - 5
        )
        self.canvas.line(
            x + width - 5, y + height - 5, x + width - 5, y + height - 5 - size
        )

        # Bottom-left corner
        self.canvas.line(x + 5, y + 5, x + 5 + size, y + 5)
        self.canvas.line(x + 5, y + 5, x + 5, y + 5 + size)

        # Bottom-right corner
        self.canvas.line(x + width - 5, y + 5, x + width - 5 - size, y + 5)
        self.canvas.line(x + width - 5, y + 5, x + width - 5, y + 5 + size)

    def draw_decorative_divider(self, x, y, width, color):
        """Draw a decorative divider line between header and content."""
        self.canvas.saveState()

        # Draw main line
        self.canvas.setStrokeColor(color)
        self.canvas.setLineWidth(1)
        self.canvas.line(x + 15, y, x + width - 15, y)

        # Draw small circles at ends
        self.canvas.setFillColor(color)
        self.canvas.circle(x + 15, y, 2, fill=1, stroke=0)
        self.canvas.circle(x + width - 15, y, 2, fill=1, stroke=0)

        self.canvas.restoreState()

    def draw_card(self, x, y, category, question):
        """Draw a complete card with all components."""
        # Get the dimension constants
        card_width = self.style_manager.card_width
        card_height = self.style_manager.card_height
        header_height = self.style_manager.header_height

        # Get colors for this category
        color_scheme = self.style_manager.get_color_scheme(category)

        # Get typography for this category - NEW
        typography = self.style_manager.get_typography(category)

        # Draw shadow for float effect
        self.draw_card_shadow(
            x,
            y,
            card_width,
            card_height,
            radius=10,
            shadow_color=color_scheme["shadow_color"],
            offset=4,
        )

        # Card border
        self.canvas.setStrokeColor(color_scheme["border_color"])
        self.canvas.setLineWidth(3)
        self.canvas.roundRect(
            x, y, card_width, card_height, radius=10, fill=0, stroke=1
        )

        # Draw gradient background
        self.draw_gradient_background(
            x + 1,
            y + 1,
            card_width - 2,
            card_height - 2,
            color_scheme["gradient_start"],
            color_scheme["gradient_end"],
            steps=15,
        )

        # Draw subtle dot pattern
        self.draw_subtle_pattern(
            x + 10,
            y + 10,
            card_width - 20,
            card_height - 20,
            color_scheme["pattern_color"],
        )

        # Draw corner accents
        self.draw_corner_accents(
            x, y, card_width, card_height, color_scheme["border_color"], size=10
        )

        # Draw header background - no border radius
        self.canvas.setFillColor(color_scheme["header"])
        self.canvas.rect(
            x + 5,
            y + card_height - header_height - 5,
            card_width - 10,
            header_height,
            fill=1,
            stroke=0,
        )

        # Draw header text with shadow - using category-specific typography
        header_font = typography["header_font"]
        header_size = typography["header_size"]
        text_width = self.canvas.stringWidth(category, header_font, header_size)
        self.draw_text_with_shadow(
            category,
            x + (card_width - text_width) / 2,
            y + card_height - (header_height / 2) - 5,  # Better vertical centering
            header_font,
            header_size,
            colors.navy,
        )

        # Draw decorative divider between header and content
        self.draw_decorative_divider(
            x,
            y + card_height - header_height - 12,
            card_width,
            color_scheme["border_color"],
        )

        # Question text - using category-specific typography
        question_font = typography["question_font"]
        question_size = typography["question_size"]
        self.canvas.setFont(question_font, question_size)
        self.canvas.setFillColor(color_scheme["text_color"])

        max_width = card_width - 20
        words = question.split()
        line = ""
        lines = []
        for word in words:
            test_line = line + word + " "
            if (
                self.canvas.stringWidth(test_line, question_font, question_size)
                <= max_width
            ):
                line = test_line
            else:
                lines.append(line.strip())
                line = word + " "
        if line:
            lines.append(line.strip())

        # Draw question text with improved vertical spacing
        start_y = y + (card_height - header_height) / 2 + (len(lines) * 8) - 5
        line_spacing = 18  # Increased from 16 for better readability

        for i, line in enumerate(lines):
            text_width = self.canvas.stringWidth(line, question_font, question_size)
            self.canvas.drawString(
                x + (card_width - text_width) / 2, start_y - i * line_spacing, line
            )

        # Add centered logo at the bottom (unchanged)
        cached_logo = self.resource_manager.get_logo()
        if cached_logo is not False:  # False means loading failed previously
            logo_width = 0.7 * inch
            logo_height = 0.7 * inch

            # Calculate appropriate logo position based on number of text lines
            min_space_above_logo = 25

            # Calculate where the last text line ends
            last_line_y = start_y - (len(lines) - 1) * line_spacing

            # Ensure logo doesn't crowd the text
            logo_y = min(y + 18, last_line_y - min_space_above_logo - logo_height)

            # Don't let logo go below the card
            if logo_y < y + 10:
                logo_y = y + 10

            logo_x = x + (card_width - logo_width) / 2  # Centered horizontally
            try:
                self.canvas.drawImage(
                    cached_logo,
                    logo_x,
                    logo_y,
                    width=logo_width,
                    height=logo_height,
                    mask="auto",
                )
            except Exception:
                # Fallback to text if there's an issue drawing the image
                self.canvas.setFont("DejaVuSans-Bold", 7)
                self.canvas.setFillColor(color_scheme["border_color"])
                text = "THE INSECT ASYLUM"
                text_width = self.canvas.stringWidth(text, "DejaVuSans-Bold", 7)
                self.canvas.drawString(x + (card_width - text_width) / 2, y + 20, text)
        else:
            # If logo loading failed, add a text identifier
            self.canvas.setFont("DejaVuSans-Bold", 7)
            self.canvas.setFillColor(color_scheme["border_color"])
            text = "THE INSECT ASYLUM"
            text_width = self.canvas.stringWidth(text, "DejaVuSans-Bold", 7)
            self.canvas.drawString(x + (card_width - text_width) / 2, y + 20, text)
