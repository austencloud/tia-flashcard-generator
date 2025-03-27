from components.resource_manager import ResourceManager
from components.card_data import CardData
from components.style_manager import StyleManager
from components.card_renderer import CardRenderer
from components.title_page_generator import TitlePageGenerator
from components.flashcard_generator import FlashcardGenerator

def main():
    """Main entry point for the flashcard generator application."""
    # Initialize the necessary components
    output_file = "nature_flashcards_premium.pdf"
    resource_manager = ResourceManager(logo_path="insect_asylum_logo.png")
    card_data = CardData()
    style_manager = StyleManager()
    
    # Create the flashcard generator
    generator = FlashcardGenerator(output_file=output_file)
    
    # Create the card renderer
    card_renderer = CardRenderer(generator.canvas, style_manager, resource_manager)
    
    # Create the title page generator
    title_page_generator = TitlePageGenerator(
        generator.canvas, 
        generator.page_width, 
        generator.page_height, 
        resource_manager,
        card_renderer
    )
    
    # Generate the cards
    generator.generate_cards(card_data, card_renderer, title_page_generator, style_manager)

if __name__ == "__main__":
    main()
