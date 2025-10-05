"""
Natural Language Processing module for pet dialogue system.
Processes user input and generates appropriate responses.
"""

import re
from typing import Tuple, Optional
import random


class NLPProcessor:
    """
    Simple NLP processor for understanding user commands and generating responses.
    Uses keyword matching and pattern recognition for command interpretation.
    """
    
    def __init__(self):
        """Initialize the NLP processor with command patterns."""
        self.command_patterns = {
            'feed': [
                r'\b(feed|food|eat|hungry|meal)\b',
                r'\bgive.*food\b',
                r'\bfeed.*pet\b'
            ],
            'play': [
                r'\b(play|game|fun|toy)\b',
                r'\bplay.*with\b',
                r'\bhave.*fun\b'
            ],
            'train': [
                r'\b(train|teach|learn|practice|study)\b',
                r'\bshow.*trick\b',
                r'\blearn.*something\b'
            ],
            'clean': [
                r'\b(clean|wash|bath|bathe|groom|shower)\b',
                r'\bgive.*bath\b',
                r'\bclean.*up\b'
            ],
            'rest': [
                r'\b(rest|sleep|nap|tired|relax)\b',
                r'\bgo.*sleep\b',
                r'\btake.*nap\b'
            ],
            'status': [
                r'\b(status|stats|how|state|check|info|information)\b',
                r'\bhow.*doing\b',
                r'\bhow.*feeling\b',
                r'\bshow.*stats\b'
            ],
            'help': [
                r'\b(help|command|what|options)\b',
                r'\bwhat.*can\b',
                r'\bwhat.*do\b'
            ]
        }
        
        self.greetings = ['hello', 'hi', 'hey', 'greetings', 'howdy']
        self.farewells = ['bye', 'goodbye', 'exit', 'quit', 'leave', 'farewell']
    
    def parse_command(self, text: str) -> Tuple[Optional[str], float]:
        """
        Parse user input to extract command intent.
        Returns: (command, confidence_score)
        """
        text_lower = text.lower().strip()
        
        # Check for exact matches first
        if text_lower in ['feed', 'play', 'train', 'clean', 'rest', 'status', 'help']:
            return text_lower, 1.0
        
        # Check for greetings
        if any(greeting in text_lower for greeting in self.greetings):
            return 'greeting', 0.9
        
        # Check for farewells
        if any(farewell in text_lower for farewell in self.farewells):
            return 'farewell', 0.9
        
        # Pattern matching for commands
        best_match = None
        best_score = 0.0
        
        for command, patterns in self.command_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    score = 0.8
                    if best_score < score:
                        best_score = score
                        best_match = command
        
        return best_match, best_score
    
    def generate_greeting(self, pet_name: str, mood: str) -> str:
        """Generate a greeting response."""
        greetings = [
            f"Hello! {pet_name} is {mood} to see you!",
            f"Hi there! {pet_name} greets you warmly!",
            f"Welcome back! {pet_name} is {mood}!",
            f"Hey! {pet_name} is happy you're here!"
        ]
        return random.choice(greetings)
    
    def generate_farewell(self, pet_name: str) -> str:
        """Generate a farewell response."""
        farewells = [
            f"Goodbye! {pet_name} will miss you!",
            f"See you later! Take care of {pet_name}!",
            f"Bye! {pet_name} hopes to see you soon!",
            f"Come back soon! {pet_name} will be waiting!"
        ]
        return random.choice(farewells)
    
    def generate_confusion_response(self, pet_name: str) -> str:
        """Generate response when command is not understood."""
        responses = [
            f"{pet_name} doesn't understand. Try 'help' to see available commands.",
            f"Sorry, {pet_name} didn't catch that. Type 'help' for options.",
            f"{pet_name} is confused. Use 'help' to see what you can do.",
            f"I don't understand. Type 'help' to see available commands."
        ]
        return random.choice(responses)
    
    def generate_talk_response(self, pet_name: str, mood: str, personality: dict) -> str:
        """
        Generate a contextual talk response based on pet's mood and personality.
        """
        if mood == "very happy":
            responses = [
                f"{pet_name}: I'm having such a wonderful time with you!",
                f"{pet_name}: Everything is amazing today!",
                f"{pet_name}: I love spending time with you!"
            ]
        elif mood == "content":
            responses = [
                f"{pet_name}: Things are going well!",
                f"{pet_name}: I'm feeling pretty good.",
                f"{pet_name}: Life is nice!"
            ]
        elif mood == "neutral":
            responses = [
                f"{pet_name}: I'm okay, I guess.",
                f"{pet_name}: Just another day.",
                f"{pet_name}: Could be better..."
            ]
        elif mood == "sad":
            responses = [
                f"{pet_name}: I'm not feeling great...",
                f"{pet_name}: Could you cheer me up?",
                f"{pet_name}: I need some attention..."
            ]
        else:  # very sad
            responses = [
                f"{pet_name}: I really need your help...",
                f"{pet_name}: Please take care of me...",
                f"{pet_name}: I'm not doing well..."
            ]
        
        # Add personality-based variations
        if personality.get('playfulness', 50) > 70:
            responses.append(f"{pet_name}: Let's play something fun!")
        
        if personality.get('curiosity', 50) > 70:
            responses.append(f"{pet_name}: I wonder what we'll do next!")
        
        return random.choice(responses)
    
    def extract_pet_name(self, text: str) -> Optional[str]:
        """
        Extract pet name from user input (e.g., "name my pet Fluffy").
        Returns the extracted name or None.
        """
        patterns = [
            r'name.*?(?:is|:|=)\s*(\w+)',
            r'call.*?(?:it|pet|them)\s*(\w+)',
            r'(?:my|the)\s*pet\s*(\w+)',
        ]
        
        text_lower = text.lower()
        for pattern in patterns:
            match = re.search(pattern, text_lower)
            if match:
                return match.group(1).capitalize()
        
        # Check if single word that could be a name
        words = text.strip().split()
        if len(words) == 1 and words[0].isalpha():
            return words[0].capitalize()
        
        return None
    
    def sentiment_analysis(self, text: str) -> str:
        """
        Simple sentiment analysis of user input.
        Returns: 'positive', 'negative', or 'neutral'
        """
        positive_words = ['good', 'great', 'awesome', 'love', 'happy', 'nice', 'excellent', 'wonderful']
        negative_words = ['bad', 'sad', 'hate', 'terrible', 'awful', 'poor', 'angry', 'upset']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
