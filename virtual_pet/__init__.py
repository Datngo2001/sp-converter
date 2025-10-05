"""
Virtual Pet Game - AI-powered virtual pet companion.

This package provides a complete virtual pet game with:
- Pet state management (mood, health, energy, etc.)
- AI-driven behavior and learning
- Natural language processing for dialogue
- State persistence between sessions
- Interactive command-line interface

Usage:
    from virtual_pet.cli import VirtualPetCLI
    
    game = VirtualPetCLI()
    game.run()

Or run directly:
    python -m virtual_pet.cli
"""

__version__ = "1.0.0"
__author__ = "Virtual Pet Game Development Team"

from virtual_pet.pet import Pet
from virtual_pet.ai_behavior import PetAI
from virtual_pet.nlp_processor import NLPProcessor
from virtual_pet.persistence import PetPersistence

__all__ = [
    'Pet',
    'PetAI',
    'NLPProcessor',
    'PetPersistence',
]
