"""
AI-driven behavior logic for the virtual pet.
Implements decision-making and adaptive learning based on interaction history.
"""

import random
from typing import List, Dict, Tuple
from collections import Counter


class PetAI:
    """
    AI behavior system for the pet using rule-based logic and reinforcement learning.
    
    The AI learns from user interactions and adapts the pet's responses accordingly.
    """
    
    def __init__(self, pet):
        """Initialize AI for the given pet."""
        self.pet = pet
        self.learning_rate = 0.1
        self.action_preferences: Dict[str, float] = {
            'feed': 0.5,
            'play': 0.5,
            'train': 0.5,
            'clean': 0.5,
            'rest': 0.5
        }
    
    def get_suggested_action(self) -> Tuple[str, str]:
        """
        Suggest an action based on pet's current state and learned preferences.
        Returns: (action, reason)
        """
        suggestions = []
        
        # Rule-based suggestions based on critical needs
        if self.pet.hunger > 70:
            suggestions.append(('feed', f"{self.pet.name} is very hungry!"))
        elif self.pet.hunger > 50:
            suggestions.append(('feed', f"{self.pet.name} is getting hungry."))
        
        if self.pet.energy < 30:
            suggestions.append(('rest', f"{self.pet.name} is very tired."))
        elif self.pet.energy < 50:
            suggestions.append(('rest', f"{self.pet.name} could use some rest."))
        
        if self.pet.cleanliness < 30:
            suggestions.append(('clean', f"{self.pet.name} really needs a bath!"))
        elif self.pet.cleanliness < 50:
            suggestions.append(('clean', f"{self.pet.name} is getting dirty."))
        
        if self.pet.mood < 40 and self.pet.energy > 30:
            suggestions.append(('play', f"{self.pet.name} seems sad and could use some fun."))
        
        # If no critical needs, suggest based on personality and learned preferences
        if not suggestions:
            if self.pet.personality['playfulness'] > 60 and self.pet.energy > 40:
                suggestions.append(('play', f"{self.pet.name} is feeling playful!"))
            
            if self.pet.personality['curiosity'] > 60 and self.pet.energy > 40:
                suggestions.append(('train', f"{self.pet.name} is eager to learn!"))
            
            # Use learned preferences
            preferred_action = max(self.action_preferences.items(), key=lambda x: x[1])
            suggestions.append((preferred_action[0], f"{self.pet.name} enjoys {preferred_action[0]}ing!"))
        
        # Return highest priority suggestion
        if suggestions:
            return suggestions[0]
        
        return ('play', f"Spend some time with {self.pet.name}!")
    
    def learn_from_interaction(self, action: str, success: bool):
        """
        Update action preferences based on interaction outcome.
        This implements a simple reinforcement learning mechanism.
        """
        if action not in self.action_preferences:
            return
        
        # Positive reinforcement for successful actions
        if success:
            self.action_preferences[action] = min(
                1.0,
                self.action_preferences[action] + self.learning_rate
            )
        else:
            # Slight negative reinforcement for failed actions
            self.action_preferences[action] = max(
                0.0,
                self.action_preferences[action] - self.learning_rate * 0.5
            )
    
    def analyze_interaction_pattern(self) -> Dict[str, any]:
        """
        Analyze the pet's interaction history to provide insights.
        Returns statistics about interaction patterns.
        """
        if not self.pet.interaction_history:
            return {
                'message': 'No interaction history yet.',
                'most_common': None,
                'total_interactions': 0
            }
        
        counter = Counter(self.pet.interaction_history)
        most_common = counter.most_common(1)[0]
        
        return {
            'message': f"You interact with {self.pet.name} most through {most_common[0]}.",
            'most_common': most_common[0],
            'frequency': most_common[1],
            'total_interactions': len(self.pet.interaction_history),
            'action_distribution': dict(counter)
        }
    
    def generate_response(self, action: str, success: bool) -> str:
        """
        Generate a contextual response based on pet personality and action outcome.
        """
        if not success:
            responses = [
                f"{self.pet.name} can't do that right now.",
                f"{self.pet.name} isn't in the mood for that.",
                f"Maybe try something else with {self.pet.name}?"
            ]
            return random.choice(responses)
        
        # Success responses vary based on personality
        if action == 'play':
            if self.pet.personality['playfulness'] > 70:
                responses = [
                    f"{self.pet.name} is having so much fun!",
                    f"{self.pet.name} loves playing with you!",
                    f"{self.pet.name} is bouncing with joy!"
                ]
            else:
                responses = [
                    f"{self.pet.name} enjoyed that.",
                    f"{self.pet.name} seems content.",
                    f"That was nice for {self.pet.name}."
                ]
        elif action == 'train':
            if self.pet.personality['curiosity'] > 70:
                responses = [
                    f"{self.pet.name} is a quick learner!",
                    f"{self.pet.name} is fascinated by this!",
                    f"{self.pet.name} can't wait to learn more!"
                ]
            else:
                responses = [
                    f"{self.pet.name} is trying their best.",
                    f"{self.pet.name} is learning steadily.",
                    f"Good progress from {self.pet.name}!"
                ]
        elif action == 'feed':
            responses = [
                f"{self.pet.name} is satisfied!",
                f"{self.pet.name} loved that meal!",
                f"Nom nom! {self.pet.name} is happy!"
            ]
        elif action == 'clean':
            responses = [
                f"{self.pet.name} is sparkling clean!",
                f"{self.pet.name} feels refreshed!",
                f"All clean! {self.pet.name} is happy!"
            ]
        elif action == 'rest':
            responses = [
                f"{self.pet.name} is well-rested now!",
                f"{self.pet.name} had a great nap!",
                f"{self.pet.name} feels energized!"
            ]
        else:
            responses = [f"{self.pet.name} appreciated that!"]
        
        return random.choice(responses)
    
    def predict_mood_change(self, action: str) -> float:
        """
        Predict how an action would affect the pet's mood.
        Returns estimated mood change.
        """
        mood_predictions = {
            'feed': 10 if self.pet.hunger > 50 else 5,
            'play': 15 if self.pet.energy > 30 else -5,
            'train': 5 if self.pet.energy > 40 else -5,
            'clean': 5,
            'rest': 10 if self.pet.energy < 50 else 0
        }
        
        return mood_predictions.get(action, 0)
    
    def to_dict(self) -> Dict:
        """Convert AI state to dictionary for serialization."""
        return {
            'action_preferences': self.action_preferences,
            'learning_rate': self.learning_rate
        }
    
    @classmethod
    def from_dict(cls, pet, data: Dict) -> 'PetAI':
        """Create AI from dictionary."""
        ai = cls(pet)
        ai.action_preferences = data.get('action_preferences', ai.action_preferences)
        ai.learning_rate = data.get('learning_rate', ai.learning_rate)
        return ai
