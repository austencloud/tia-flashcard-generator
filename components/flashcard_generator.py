import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class FlashcardGenerator:
    """Main class for coordinating the flashcard generation process."""
    
    def __init__(self, output_file="nature_flashcards_premium.pdf"):
        self.output_file = output_file
        self.page_width, self.page_height = letter
        
        # Layout settings
        self.cols = 2
        self.rows = 5
        self.cards_per_page = self.cols * self.rows
        
        # Create canvas
        self.canvas = canvas.Canvas(output_file, pagesize=letter)
    
    def generate_cards(self, card_data, card_renderer, title_page_generator, style_manager):
        """Generate the PDF with title page and cards."""
        # Create the title page first
        title_page_generator.create_title_page()
        self.canvas.showPage()
        
        # Calculate margins
        margin_x = (self.page_width - (self.cols * style_manager.card_width)) / 2
        margin_y = (self.page_height - (self.rows * style_manager.card_height)) / 2
        
        # Generate all the flashcards
        cards = card_data.get_all_cards()
        for i, (category, question) in enumerate(cards):
            page_index = i % self.cards_per_page
            col = page_index % self.cols
            row = page_index // self.cols
        
            x = margin_x + col * style_manager.card_width
            y = self.page_height - margin_y - (row + 1) * style_manager.card_height
        
            card_renderer.draw_card(x, y, category, question)
        
            if (i + 1) % self.cards_per_page == 0:
                self.canvas.showPage()
        
        # Final page if needed
        if len(cards) % self.cards_per_page != 0:
            self.canvas.showPage()
        
        # Save the PDF
        self.canvas.save()
        print(f"✨ The Insect Asylum nature flashcards saved to: {os.path.abspath(self.output_file)}")
