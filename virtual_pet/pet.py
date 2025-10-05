"""
Core Pet class for the virtual pet game.
Manages pet state including mood, health, energy, hunger, and cleanliness.
"""

import time
from typing import Dict, List, Tuple
import random


class Pet:
    """
    Virtual pet with AI-driven behavior and state management.
    
    Attributes:
        name: Pet's name
        mood: Current mood level (0-100)
        health: Current health level (0-100)
        energy: Current energy level (0-100)
        hunger: Current hunger level (0-100, higher means more hungry)
        cleanliness: Current cleanliness level (0-100)
        personality: Dictionary tracking personality traits
        experience: Experience points from training
        last_update: Timestamp of last state update
    """
    
    def __init__(self, name: str):
        """Initialize a new pet with the given name."""
        self.name = name
        self.mood = 70.0
        self.health = 100.0
        self.energy = 80.0
        self.hunger = 30.0
        self.cleanliness = 90.0
        self.personality = {
            'playfulness': 50.0,
            'friendliness': 50.0,
            'independence': 50.0,
            'curiosity': 50.0
        }
        self.experience = 0
        self.last_update = time.time()
        self.interaction_history: List[str] = []
    
    def update_state(self):
        """Update pet state based on time passed since last update."""
        current_time = time.time()
        time_passed = (current_time - self.last_update) / 60  # minutes
        
        # Natural decay over time
        self.hunger = min(100.0, self.hunger + time_passed * 0.5)
        self.energy = max(0.0, self.energy - time_passed * 0.3)
        self.cleanliness = max(0.0, self.cleanliness - time_passed * 0.2)
        
        # Mood affected by other stats
        mood_change = 0
        if self.hunger > 70:
            mood_change -= 0.5
        if self.energy < 30:
            mood_change -= 0.3
        if self.cleanliness < 40:
            mood_change -= 0.2
        if self.health < 50:
            mood_change -= 0.5
            
        self.mood = max(0.0, min(100.0, self.mood + mood_change * time_passed))
        
        # Health affected by extreme stats
        if self.hunger > 90 or self.cleanliness < 20:
            self.health = max(0.0, self.health - 0.1 * time_passed)
        
        self.last_update = current_time
    
    def feed(self) -> Tuple[bool, str]:
        """Feed the pet to reduce hunger."""
        self.update_state()
        
        if self.hunger < 20:
            return False, f"{self.name} is not hungry right now!"
        
        hunger_reduction = random.uniform(30, 50)
        self.hunger = max(0.0, self.hunger - hunger_reduction)
        self.energy = min(100.0, self.energy + 5)
        self.mood = min(100.0, self.mood + 10)
        
        self.interaction_history.append('feed')
        
        return True, f"{self.name} enjoyed the meal! Hunger reduced significantly."
    
    def play(self) -> Tuple[bool, str]:
        """Play with the pet to improve mood."""
        self.update_state()
        
        if self.energy < 20:
            return False, f"{self.name} is too tired to play right now."
        
        energy_cost = random.uniform(15, 25)
        self.energy = max(0.0, self.energy - energy_cost)
        self.mood = min(100.0, self.mood + 15)
        self.hunger = min(100.0, self.hunger + 5)
        
        # Playing increases playfulness personality trait
        self.personality['playfulness'] = min(100.0, self.personality['playfulness'] + 0.5)
        
        self.interaction_history.append('play')
        
        return True, f"{self.name} had a great time playing! Mood improved but got a bit tired."
    
    def train(self) -> Tuple[bool, str]:
        """Train the pet to gain experience."""
        self.update_state()
        
        if self.energy < 30:
            return False, f"{self.name} is too tired for training."
        
        energy_cost = random.uniform(20, 30)
        self.energy = max(0.0, self.energy - energy_cost)
        exp_gain = random.randint(5, 15)
        self.experience += exp_gain
        self.hunger = min(100.0, self.hunger + 10)
        
        # Training increases independence and curiosity
        self.personality['independence'] = min(100.0, self.personality['independence'] + 0.3)
        self.personality['curiosity'] = min(100.0, self.personality['curiosity'] + 0.4)
        
        self.interaction_history.append('train')
        
        return True, f"{self.name} learned something new! Gained {exp_gain} experience."
    
    def clean(self) -> Tuple[bool, str]:
        """Clean the pet to improve cleanliness."""
        self.update_state()
        
        if self.cleanliness > 80:
            return False, f"{self.name} is already very clean!"
        
        cleanliness_gain = random.uniform(30, 50)
        self.cleanliness = min(100.0, self.cleanliness + cleanliness_gain)
        self.mood = min(100.0, self.mood + 5)
        
        self.interaction_history.append('clean')
        
        return True, f"{self.name} feels fresh and clean now!"
    
    def rest(self) -> Tuple[bool, str]:
        """Let the pet rest to restore energy."""
        self.update_state()
        
        if self.energy > 80:
            return False, f"{self.name} is not tired right now."
        
        energy_gain = random.uniform(40, 60)
        self.energy = min(100.0, self.energy + energy_gain)
        self.hunger = min(100.0, self.hunger + 5)
        
        self.interaction_history.append('rest')
        
        return True, f"{self.name} took a good nap and feels refreshed!"
    
    def get_status(self) -> Dict[str, float]:
        """Get current pet status."""
        self.update_state()
        return {
            'mood': round(self.mood, 1),
            'health': round(self.health, 1),
            'energy': round(self.energy, 1),
            'hunger': round(self.hunger, 1),
            'cleanliness': round(self.cleanliness, 1),
            'experience': self.experience
        }
    
    def get_personality(self) -> Dict[str, float]:
        """Get current personality traits."""
        return {k: round(v, 1) for k, v in self.personality.items()}
    
    def get_mood_description(self) -> str:
        """Get a text description of the pet's current mood."""
        self.update_state()
        
        if self.mood >= 80:
            return "very happy"
        elif self.mood >= 60:
            return "content"
        elif self.mood >= 40:
            return "neutral"
        elif self.mood >= 20:
            return "sad"
        else:
            return "very sad"
    
    def to_dict(self) -> Dict:
        """Convert pet state to dictionary for serialization."""
        return {
            'name': self.name,
            'mood': self.mood,
            'health': self.health,
            'energy': self.energy,
            'hunger': self.hunger,
            'cleanliness': self.cleanliness,
            'personality': self.personality,
            'experience': self.experience,
            'last_update': self.last_update,
            'interaction_history': self.interaction_history[-50:]  # Keep last 50 interactions
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Pet':
        """Create pet from dictionary."""
        pet = cls(data['name'])
        pet.mood = data.get('mood', 70.0)
        pet.health = data.get('health', 100.0)
        pet.energy = data.get('energy', 80.0)
        pet.hunger = data.get('hunger', 30.0)
        pet.cleanliness = data.get('cleanliness', 90.0)
        pet.personality = data.get('personality', pet.personality)
        pet.experience = data.get('experience', 0)
        pet.last_update = data.get('last_update', time.time())
        pet.interaction_history = data.get('interaction_history', [])
        return pet
