#!/usr/bin/env python3
"""
Command-line interface for the Virtual Pet Game.
Provides an interactive experience for users to care for their virtual pet.
"""

import sys
import os
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from virtual_pet.pet import Pet
from virtual_pet.ai_behavior import PetAI
from virtual_pet.nlp_processor import NLPProcessor
from virtual_pet.persistence import PetPersistence


class VirtualPetCLI:
    """Command-line interface for the virtual pet game."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.pet: Optional[Pet] = None
        self.ai: Optional[PetAI] = None
        self.nlp = NLPProcessor()
        self.persistence = PetPersistence()
        self.running = False
    
    def display_banner(self):
        """Display welcome banner."""
        print("\n" + "=" * 60)
        print("      🐾 VIRTUAL PET GAME - AI-Powered Companion 🐾")
        print("=" * 60)
        print()
    
    def display_help(self):
        """Display available commands."""
        print("\n📋 Available Commands:")
        print("  feed      - Feed your pet")
        print("  play      - Play with your pet")
        print("  train     - Train your pet")
        print("  clean     - Clean your pet")
        print("  rest      - Let your pet rest")
        print("  talk      - Talk to your pet")
        print("  status    - Check pet's status")
        print("  suggest   - Get AI suggestion for next action")
        print("  stats     - View interaction statistics")
        print("  save      - Save your pet")
        print("  load      - Load a saved pet")
        print("  help      - Show this help message")
        print("  quit/exit - Exit the game")
        print()
    
    def display_status(self, detailed: bool = False):
        """Display pet status."""
        if not self.pet:
            print("❌ No pet loaded!")
            return
        
        status = self.pet.get_status()
        personality = self.pet.get_personality()
        mood_desc = self.pet.get_mood_description()
        
        print(f"\n🐾 {self.pet.name}'s Status:")
        print("=" * 50)
        print(f"  Mood:        {'█' * int(status['mood'] / 5)} {status['mood']}% ({mood_desc})")
        print(f"  Health:      {'█' * int(status['health'] / 5)} {status['health']}%")
        print(f"  Energy:      {'█' * int(status['energy'] / 5)} {status['energy']}%")
        print(f"  Hunger:      {'█' * int(status['hunger'] / 5)} {status['hunger']}%")
        print(f"  Cleanliness: {'█' * int(status['cleanliness'] / 5)} {status['cleanliness']}%")
        print(f"  Experience:  {status['experience']} XP")
        
        if detailed:
            print("\n🎭 Personality Traits:")
            for trait, value in personality.items():
                print(f"  {trait.capitalize():15} {'█' * int(value / 5)} {value}%")
        
        print()
    
    def create_new_pet(self):
        """Create a new pet."""
        print("\n🐣 Let's create your new pet!")
        while True:
            name = input("What would you like to name your pet? ").strip()
            if name:
                self.pet = Pet(name)
                self.ai = PetAI(self.pet)
                print(f"\n✨ {name} has been created!")
                self.display_status()
                return
            print("Please enter a valid name.")
    
    def load_pet_menu(self):
        """Show load menu and load a pet."""
        saves = self.persistence.list_saves()
        
        if not saves:
            print("\n❌ No saved pets found!")
            return False
        
        print("\n📂 Available Saves:")
        for i, save_name in enumerate(saves, 1):
            info = self.persistence.get_save_info(save_name)
            if info:
                print(f"  {i}. {info['name']} - XP: {info['experience']}, Mood: {info['mood']}%")
        
        print("\nEnter the number or name of the save to load (or 'cancel' to go back):")
        choice = input("> ").strip()
        
        if choice.lower() == 'cancel':
            return False
        
        try:
            # Try to parse as number
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(saves):
                    save_name = saves[idx]
                else:
                    print("❌ Invalid selection!")
                    return False
            else:
                save_name = choice
            
            self.pet, self.ai = self.persistence.load_pet(save_name)
            print(f"\n✅ Loaded {self.pet.name}!")
            self.display_status()
            return True
        
        except FileNotFoundError:
            print("❌ Save file not found!")
            return False
        except Exception as e:
            print(f"❌ Error loading save: {e}")
            return False
    
    def save_pet(self):
        """Save the current pet."""
        if not self.pet:
            print("❌ No pet to save!")
            return
        
        filepath = self.persistence.save_pet(self.pet, self.ai)
        print(f"✅ {self.pet.name} has been saved to {filepath}")
    
    def handle_action(self, action: str) -> bool:
        """
        Handle a pet action.
        Returns True if action was successful.
        """
        action_map = {
            'feed': self.pet.feed,
            'play': self.pet.play,
            'train': self.pet.train,
            'clean': self.pet.clean,
            'rest': self.pet.rest
        }
        
        if action in action_map:
            success, message = action_map[action]()
            print(f"\n{message}")
            
            if self.ai:
                self.ai.learn_from_interaction(action, success)
                ai_response = self.ai.generate_response(action, success)
                print(f"💭 {ai_response}")
            
            return success
        
        return False
    
    def show_suggestion(self):
        """Show AI suggestion for next action."""
        if not self.ai:
            print("❌ AI not available!")
            return
        
        action, reason = self.ai.get_suggested_action()
        print(f"\n💡 AI Suggestion: {action}")
        print(f"   Reason: {reason}")
        
        mood_change = self.ai.predict_mood_change(action)
        if mood_change > 0:
            print(f"   Expected mood change: +{mood_change}%")
        elif mood_change < 0:
            print(f"   Expected mood change: {mood_change}%")
    
    def show_stats(self):
        """Show interaction statistics."""
        if not self.ai:
            print("❌ AI not available!")
            return
        
        stats = self.ai.analyze_interaction_pattern()
        print(f"\n📊 Interaction Statistics:")
        print(f"  Total interactions: {stats['total_interactions']}")
        
        if stats['most_common']:
            print(f"  Most common action: {stats['most_common']} ({stats['frequency']} times)")
        
        if 'action_distribution' in stats:
            print("\n  Action distribution:")
            for action, count in stats['action_distribution'].items():
                print(f"    {action}: {count} times")
    
    def talk_to_pet(self):
        """Have a conversation with the pet."""
        if not self.pet:
            print("❌ No pet loaded!")
            return
        
        mood_desc = self.pet.get_mood_description()
        personality = self.pet.get_personality()
        
        response = self.nlp.generate_talk_response(
            self.pet.name,
            mood_desc,
            personality
        )
        print(f"\n💬 {response}")
    
    def process_command(self, user_input: str) -> bool:
        """
        Process user command.
        Returns False if user wants to quit.
        """
        if not user_input:
            return True
        
        # Parse with NLP
        command, confidence = self.nlp.parse_command(user_input)
        
        # Handle special commands
        if command == 'greeting':
            mood_desc = self.pet.get_mood_description() if self.pet else "happy"
            pet_name = self.pet.name if self.pet else "your pet"
            print(f"\n{self.nlp.generate_greeting(pet_name, mood_desc)}")
            return True
        
        if command == 'farewell':
            pet_name = self.pet.name if self.pet else "your pet"
            print(f"\n{self.nlp.generate_farewell(pet_name)}")
            
            if self.pet:
                print("\n💾 Don't forget to save your pet before leaving!")
                save_choice = input("Would you like to save now? (yes/no): ").strip().lower()
                if save_choice in ['yes', 'y']:
                    self.save_pet()
            
            return False
        
        if not self.pet and command not in ['help', 'load', None]:
            print("\n❌ Please create or load a pet first!")
            return True
        
        # Handle commands
        if command == 'help':
            self.display_help()
        elif command == 'status':
            self.display_status(detailed=True)
        elif command in ['feed', 'play', 'train', 'clean', 'rest']:
            self.handle_action(command)
            # Show brief status after action
            status = self.pet.get_status()
            print(f"   Mood: {status['mood']}% | Energy: {status['energy']}% | Hunger: {status['hunger']}%")
        elif user_input.lower() == 'talk':
            self.talk_to_pet()
        elif user_input.lower() == 'suggest':
            self.show_suggestion()
        elif user_input.lower() == 'stats':
            self.show_stats()
        elif user_input.lower() == 'save':
            self.save_pet()
        elif user_input.lower() == 'load':
            self.load_pet_menu()
        elif confidence < 0.5:
            pet_name = self.pet.name if self.pet else "Pet"
            print(f"\n{self.nlp.generate_confusion_response(pet_name)}")
        
        return True
    
    def run(self):
        """Run the main game loop."""
        self.display_banner()
        
        print("Would you like to:")
        print("  1. Create a new pet")
        print("  2. Load an existing pet")
        print("\nEnter your choice (1 or 2):")
        
        choice = input("> ").strip()
        
        if choice == '1':
            self.create_new_pet()
        elif choice == '2':
            if not self.load_pet_menu():
                print("\nStarting with a new pet instead...")
                self.create_new_pet()
        else:
            print("Invalid choice. Starting with a new pet...")
            self.create_new_pet()
        
        self.display_help()
        
        self.running = True
        print("\n💬 You can type commands or talk naturally to your pet!")
        print("   (Type 'help' anytime to see available commands)\n")
        
        while self.running:
            try:
                user_input = input(f"🎮 [{self.pet.name}] > ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    self.running = self.process_command('quit')
                else:
                    self.running = self.process_command(user_input)
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                if self.pet:
                    print(f"💾 Don't forget your pet {self.pet.name} will miss you!")
                break
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                print("Please try again.")
        
        print("\n✨ Thanks for playing! Come back soon! ✨\n")


def main():
    """Main entry point."""
    game = VirtualPetCLI()
    game.run()


if __name__ == "__main__":
    main()
