#!/usr/bin/env python3
"""Quick demo of the virtual pet game."""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from virtual_pet import Pet, PetAI, NLPProcessor, PetPersistence

def demo():
    """Run a quick demo of the virtual pet."""
    print("=" * 60)
    print("   VIRTUAL PET GAME - Quick Demo")
    print("=" * 60)
    print()
    
    # Create a pet
    print("Creating a new pet named 'Demo'...")
    pet = Pet("Demo")
    ai = PetAI(pet)
    nlp = NLPProcessor()
    
    # Show initial status
    print("\n📊 Initial Status:")
    status = pet.get_status()
    for key, value in status.items():
        print(f"  {key}: {value}")
    
    # Perform some actions
    print("\n🎮 Performing actions...")
    
    print("\n1. Feeding Demo...")
    pet.hunger = 60.0
    success, message = pet.feed()
    print(f"   {message}")
    ai.learn_from_interaction('feed', success)
    
    print("\n2. Playing with Demo...")
    pet.energy = 70.0
    success, message = pet.play()
    print(f"   {message}")
    print(f"   {ai.generate_response('play', success)}")
    ai.learn_from_interaction('play', success)
    
    print("\n3. Training Demo...")
    pet.energy = 60.0
    success, message = pet.train()
    print(f"   {message}")
    ai.learn_from_interaction('train', success)
    
    # Get AI suggestion
    print("\n💡 AI Suggestion:")
    action, reason = ai.get_suggested_action()
    print(f"   Action: {action}")
    print(f"   Reason: {reason}")
    
    # Show interaction stats
    print("\n📈 Interaction Statistics:")
    stats = ai.analyze_interaction_pattern()
    print(f"   Total interactions: {stats['total_interactions']}")
    print(f"   Most common: {stats.get('most_common', 'N/A')}")
    
    # Test NLP
    print("\n💬 Testing NLP:")
    test_phrases = [
        "I want to feed my pet",
        "let's play!",
        "how is Demo doing?",
        "hello"
    ]
    for phrase in test_phrases:
        command, confidence = nlp.parse_command(phrase)
        print(f"   '{phrase}' -> {command} (confidence: {confidence:.2f})")
    
    # Test persistence
    print("\n💾 Testing Persistence:")
    persistence = PetPersistence("demo_saves")
    save_path = persistence.save_pet(pet, ai, "demo_test")
    print(f"   Saved to: {save_path}")
    
    loaded_pet, loaded_ai = persistence.load_pet("demo_test")
    print(f"   Loaded pet: {loaded_pet.name}")
    print(f"   Experience: {loaded_pet.experience}")
    
    # Show final status
    print("\n📊 Final Status:")
    status = pet.get_status()
    personality = pet.get_personality()
    print(f"  Mood: {status['mood']}% ({pet.get_mood_description()})")
    print(f"  Health: {status['health']}%")
    print(f"  Energy: {status['energy']}%")
    print(f"  Hunger: {status['hunger']}%")
    print(f"  Experience: {status['experience']} XP")
    print("\n  Personality:")
    for trait, value in personality.items():
        print(f"    {trait}: {value}")
    
    # Cleanup
    import shutil
    if os.path.exists("demo_saves"):
        shutil.rmtree("demo_saves")
    
    print("\n✅ Demo completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    demo()
