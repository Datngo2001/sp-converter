#!/usr/bin/env python3
"""
Validation script to test edge cases and error handling.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from virtual_pet import Pet, PetAI, NLPProcessor, PetPersistence
import shutil

def validate_edge_cases():
    """Test edge cases and error handling."""
    print("🔍 Running validation tests...\n")
    
    passed = 0
    failed = 0
    
    # Test 1: Extreme values
    print("1. Testing extreme state values...")
    try:
        pet = Pet("EdgeCase")
        pet.hunger = 100.0
        pet.energy = 0.0
        pet.update_state()
        assert 0 <= pet.mood <= 100, "Mood out of bounds"
        assert 0 <= pet.health <= 100, "Health out of bounds"
        print("   ✅ Extreme values handled correctly")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
    
    # Test 2: Invalid actions
    print("2. Testing invalid action attempts...")
    try:
        pet = Pet("TestPet")
        pet.hunger = 10.0
        success, msg = pet.feed()
        assert not success, "Should not allow feeding when not hungry"
        
        pet.energy = 10.0
        success, msg = pet.play()
        assert not success, "Should not allow playing when too tired"
        print("   ✅ Invalid actions properly rejected")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
    
    # Test 3: Time decay
    print("3. Testing time-based state decay...")
    try:
        import time
        pet = Pet("DecayTest")
        initial_hunger = pet.hunger
        pet.last_update = time.time() - 300  # 5 minutes ago
        pet.update_state()
        assert pet.hunger > initial_hunger, "Hunger should increase over time"
        print("   ✅ Time decay working correctly")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
    
    # Test 4: AI bounds checking
    print("4. Testing AI preference bounds...")
    try:
        pet = Pet("AITest")
        ai = PetAI(pet)
        
        # Try to push preferences beyond bounds
        for _ in range(20):
            ai.learn_from_interaction('play', True)
        
        assert ai.action_preferences['play'] <= 1.0, "Preference should not exceed 1.0"
        
        for _ in range(30):
            ai.learn_from_interaction('feed', False)
        
        assert ai.action_preferences['feed'] >= 0.0, "Preference should not go below 0.0"
        print("   ✅ AI preferences bounded correctly")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
    
    # Test 5: NLP with empty/invalid input
    print("5. Testing NLP with edge case inputs...")
    try:
        nlp = NLPProcessor()
        
        command, conf = nlp.parse_command("")
        assert command is None or conf < 0.5, "Empty input should not parse"
        
        command, conf = nlp.parse_command("asdfghjkl zxcvbnm")
        assert conf < 0.5, "Gibberish should have low confidence"
        
        print("   ✅ NLP handles edge cases properly")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
    
    # Test 6: Persistence with special characters
    print("6. Testing persistence with special characters...")
    try:
        test_dir = "validation_test_saves"
        persistence = PetPersistence(test_dir)
        pet = Pet("Test-Pet_123")
        
        filepath = persistence.save_pet(pet, None, "test_special")
        assert os.path.exists(filepath), "Save file not created"
        
        loaded_pet, _ = persistence.load_pet("test_special")
        assert loaded_pet.name == "Test-Pet_123", "Name not preserved"
        
        # Cleanup
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
        
        print("   ✅ Persistence handles special characters")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
        if os.path.exists("validation_test_saves"):
            shutil.rmtree("validation_test_saves")
    
    # Test 7: Personality bounds
    print("7. Testing personality trait bounds...")
    try:
        pet = Pet("PersonalityTest")
        
        # Play many times to increase playfulness
        for _ in range(100):
            pet.energy = 50.0
            pet.play()
        
        assert 0 <= pet.personality['playfulness'] <= 100, "Playfulness out of bounds"
        print("   ✅ Personality traits bounded correctly")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
    
    # Test 8: Serialization/Deserialization integrity
    print("8. Testing data integrity through save/load cycle...")
    try:
        test_dir = "validation_integrity_test"
        persistence = PetPersistence(test_dir)
        
        original_pet = Pet("IntegrityTest")
        original_pet.mood = 65.5
        original_pet.experience = 150
        original_pet.personality['playfulness'] = 75.3
        original_pet.interaction_history = ['feed', 'play', 'train']
        
        ai = PetAI(original_pet)
        ai.action_preferences['play'] = 0.75
        
        persistence.save_pet(original_pet, ai, "integrity")
        loaded_pet, loaded_ai = persistence.load_pet("integrity")
        
        assert loaded_pet.mood == original_pet.mood, "Mood not preserved"
        assert loaded_pet.experience == original_pet.experience, "Experience not preserved"
        assert loaded_pet.personality['playfulness'] == original_pet.personality['playfulness'], "Personality not preserved"
        assert len(loaded_pet.interaction_history) == len(original_pet.interaction_history), "History not preserved"
        assert loaded_ai.action_preferences['play'] == 0.75, "AI preferences not preserved"
        
        # Cleanup
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
        
        print("   ✅ Data integrity maintained through save/load")
        passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        failed += 1
        if os.path.exists("validation_integrity_test"):
            shutil.rmtree("validation_integrity_test")
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Validation Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("✅ All validation tests passed!")
        return True
    else:
        print("❌ Some validation tests failed!")
        return False

if __name__ == "__main__":
    success = validate_edge_cases()
    sys.exit(0 if success else 1)
