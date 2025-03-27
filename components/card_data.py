class CardData:
    """Manages flashcard content including categories and questions."""
    
    def __init__(self):
        self.cards = [
            # Original categories with enhanced questions
            ("Nature Detectives", "How does it feel in your hand?"),
            ("Nature Detectives", "What colors pop out at you?"),
            ("Nature Detectives", "Does it remind you of something else?"),
            ("Nature Detectives", "What's the coolest thing about it?"),
            
            ("Animal Treasures", "Which animal left this behind?"),
            ("Animal Treasures", "How did this help the animal live?"),
            ("Animal Treasures", "Was the animal big or tiny?"),
            ("Animal Treasures", "How did the animal use this?"),
            
            ("Nature's Art", "What cool shapes do you see?"),
            ("Nature's Art", "Can you find a pattern that repeats?"),
            ("Nature's Art", "Is it the same on all sides?"),
            ("Nature's Art", "Which part looks the most special?"),
            
            ("Super Senses", "Does it feel heavy or light?"),
            ("Super Senses", "What sound does it make when tapped?"),
            ("Super Senses", "What does it smell like?"),
            ("Super Senses", "Is it smooth or bumpy?"),
            
            ("Mystery Box", "Can you guess what this is?"),
            ("Mystery Box", "Why is it shaped this way?"),
            ("Mystery Box", "What job did it do in nature?"),
            ("Mystery Box", "What clues can you find?"),
            
            ("Wild Homes", "Where did this animal live?"),
            ("Wild Homes", "How did it stay safe?"),
            ("Wild Homes", "What weather did it face?"),
            ("Wild Homes", "Who were its neighbors in nature?"),
            
            # New categories with great questions
            ("Time Machine", "How old might this be?"),
            ("Time Machine", "How has it changed over time?"),
            ("Time Machine", "What made it look this way?"),
            ("Time Machine", "What story does it tell?"),
            
            ("Texture Explorers", "Smooth or bumpy?"),
            ("Texture Explorers", "Hard or squishy?"),
            ("Texture Explorers", "How many textures can you find?"),
            ("Texture Explorers", "What happens when you touch it?"),
            
            ("Compare & Contrast", "How is this different from that one?"),
            ("Compare & Contrast", "Which is heavier and why?"),
            ("Compare & Contrast", "What do these have in common?"),
            ("Compare & Contrast", "Which would last longer in nature?"),
            
            ("Nature's Helpers", "How does this help other animals?"),
            ("Nature's Helpers", "What job does this do in nature?"),
            ("Nature's Helpers", "How does it fit in its ecosystem?"),
            ("Nature's Helpers", "Who depends on this to survive?"),
            
            # Thought-provoking questions that still work for kids
            ("Nature's Puzzles", "Why is it shaped exactly this way?"),
            ("Nature's Puzzles", "What problem did this solve in nature?"),
            ("Nature's Puzzles", "How would it be different if it lived elsewhere?"),
            ("Nature's Puzzles", "What secrets is it keeping?"),
            
            ("Imagination Station", "If this could talk, what would it say?"),
            ("Imagination Station", "What animal would want this as a home?"),
            ("Imagination Station", "If you were tiny, how would you use this?"),
            ("Imagination Station", "What would you name this if you discovered it?"),
        ]
    
    def get_all_cards(self):
        """Return all cards."""
        return self.cards
    
    def get_card_count(self):
        """Return the total number of cards."""
        return len(self.cards)
    
    def get_categories(self):
        """Return a set of all unique categories."""
        return set(category for category, _ in self.cards)
    
    def get_cards_by_category(self, category):
        """Return all questions for a given category."""
        return [question for cat, question in self.cards if cat == category]
