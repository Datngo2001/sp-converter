"""
Test suite for the Virtual Pet Game.
Tests core functionality including pet state, AI behavior, NLP, and persistence.
"""

import unittest
import time
import os
import shutil
from pathlib import Path

# Add parent directory to path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from virtual_pet.pet import Pet
from virtual_pet.ai_behavior import PetAI
from virtual_pet.nlp_processor import NLPProcessor
from virtual_pet.persistence import PetPersistence


class TestPet(unittest.TestCase):
    """Test cases for the Pet class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.pet = Pet("TestPet")
    
    def test_pet_creation(self):
        """Test pet is created with correct initial state."""
        self.assertEqual(self.pet.name, "TestPet")
        self.assertEqual(self.pet.mood, 70.0)
        self.assertEqual(self.pet.health, 100.0)
        self.assertEqual(self.pet.energy, 80.0)
        self.assertEqual(self.pet.hunger, 30.0)
        self.assertEqual(self.pet.cleanliness, 90.0)
        self.assertEqual(self.pet.experience, 0)
    
    def test_feed_action(self):
        """Test feeding the pet."""
        self.pet.hunger = 50.0
        success, message = self.pet.feed()
        self.assertTrue(success)
        self.assertLess(self.pet.hunger, 50.0)
        self.assertIn('feed', self.pet.interaction_history)
    
    def test_feed_when_not_hungry(self):
        """Test feeding when pet is not hungry."""
        self.pet.hunger = 10.0
        success, message = self.pet.feed()
        self.assertFalse(success)
        self.assertIn("not hungry", message)
    
    def test_play_action(self):
        """Test playing with the pet."""
        self.pet.energy = 50.0
        initial_mood = self.pet.mood
        success, message = self.pet.play()
        self.assertTrue(success)
        self.assertLess(self.pet.energy, 50.0)
        self.assertGreater(self.pet.mood, initial_mood)
        self.assertIn('play', self.pet.interaction_history)
    
    def test_play_when_tired(self):
        """Test playing when pet is too tired."""
        self.pet.energy = 10.0
        success, message = self.pet.play()
        self.assertFalse(success)
        self.assertIn("too tired", message)
    
    def test_train_action(self):
        """Test training the pet."""
        self.pet.energy = 50.0
        initial_exp = self.pet.experience
        success, message = self.pet.train()
        self.assertTrue(success)
        self.assertGreater(self.pet.experience, initial_exp)
        self.assertIn('train', self.pet.interaction_history)
    
    def test_clean_action(self):
        """Test cleaning the pet."""
        self.pet.cleanliness = 50.0
        success, message = self.pet.clean()
        self.assertTrue(success)
        self.assertGreater(self.pet.cleanliness, 50.0)
        self.assertIn('clean', self.pet.interaction_history)
    
    def test_rest_action(self):
        """Test resting the pet."""
        self.pet.energy = 30.0
        success, message = self.pet.rest()
        self.assertTrue(success)
        self.assertGreater(self.pet.energy, 30.0)
        self.assertIn('rest', self.pet.interaction_history)
    
    def test_state_update(self):
        """Test that pet state updates over time."""
        initial_hunger = self.pet.hunger
        initial_energy = self.pet.energy
        
        # Simulate time passing
        self.pet.last_update = time.time() - 120  # 2 minutes ago
        self.pet.update_state()
        
        self.assertGreater(self.pet.hunger, initial_hunger)
        self.assertLess(self.pet.energy, initial_energy)
    
    def test_get_status(self):
        """Test getting pet status."""
        status = self.pet.get_status()
        self.assertIn('mood', status)
        self.assertIn('health', status)
        self.assertIn('energy', status)
        self.assertIn('hunger', status)
        self.assertIn('cleanliness', status)
        self.assertIn('experience', status)
    
    def test_get_personality(self):
        """Test getting personality traits."""
        personality = self.pet.get_personality()
        self.assertIn('playfulness', personality)
        self.assertIn('friendliness', personality)
        self.assertIn('independence', personality)
        self.assertIn('curiosity', personality)
    
    def test_mood_description(self):
        """Test mood description generation."""
        self.pet.mood = 90.0
        self.assertEqual(self.pet.get_mood_description(), "very happy")
        
        self.pet.mood = 65.0
        self.assertEqual(self.pet.get_mood_description(), "content")
        
        self.pet.mood = 45.0
        self.assertEqual(self.pet.get_mood_description(), "neutral")
        
        self.pet.mood = 25.0
        self.assertEqual(self.pet.get_mood_description(), "sad")
        
        self.pet.mood = 10.0
        self.assertEqual(self.pet.get_mood_description(), "very sad")
    
    def test_personality_development(self):
        """Test that personality develops through interactions."""
        initial_playfulness = self.pet.personality['playfulness']
        
        # Play multiple times
        for _ in range(5):
            self.pet.energy = 50.0
            self.pet.play()
        
        self.assertGreater(self.pet.personality['playfulness'], initial_playfulness)
    
    def test_to_dict(self):
        """Test converting pet to dictionary."""
        pet_dict = self.pet.to_dict()
        self.assertEqual(pet_dict['name'], "TestPet")
        self.assertIn('mood', pet_dict)
        self.assertIn('personality', pet_dict)
    
    def test_from_dict(self):
        """Test creating pet from dictionary."""
        pet_dict = {
            'name': 'LoadedPet',
            'mood': 85.0,
            'health': 95.0,
            'energy': 70.0,
            'hunger': 25.0,
            'cleanliness': 88.0,
            'personality': {'playfulness': 65.0, 'friendliness': 55.0, 'independence': 45.0, 'curiosity': 60.0},
            'experience': 100,
            'last_update': time.time(),
            'interaction_history': ['feed', 'play']
        }
        
        loaded_pet = Pet.from_dict(pet_dict)
        self.assertEqual(loaded_pet.name, 'LoadedPet')
        self.assertEqual(loaded_pet.mood, 85.0)
        self.assertEqual(loaded_pet.experience, 100)


class TestPetAI(unittest.TestCase):
    """Test cases for the PetAI class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.pet = Pet("AIPet")
        self.ai = PetAI(self.pet)
    
    def test_ai_creation(self):
        """Test AI is created with correct initial state."""
        self.assertEqual(self.ai.pet, self.pet)
        self.assertEqual(self.ai.learning_rate, 0.1)
        self.assertIn('feed', self.ai.action_preferences)
    
    def test_get_suggestion_hungry(self):
        """Test AI suggests feeding when pet is hungry."""
        self.pet.hunger = 80.0
        action, reason = self.ai.get_suggested_action()
        self.assertEqual(action, 'feed')
        self.assertIn('hungry', reason.lower())
    
    def test_get_suggestion_tired(self):
        """Test AI suggests resting when pet is tired."""
        self.pet.energy = 20.0
        self.pet.hunger = 30.0  # Not critical
        action, reason = self.ai.get_suggested_action()
        self.assertEqual(action, 'rest')
        self.assertIn('tired', reason.lower())
    
    def test_get_suggestion_dirty(self):
        """Test AI suggests cleaning when pet is dirty."""
        self.pet.cleanliness = 25.0
        self.pet.hunger = 30.0
        self.pet.energy = 50.0
        action, reason = self.ai.get_suggested_action()
        self.assertEqual(action, 'clean')
        self.assertIn('bath', reason.lower())
    
    def test_learn_from_interaction_success(self):
        """Test AI learns from successful interactions."""
        initial_pref = self.ai.action_preferences['play']
        self.ai.learn_from_interaction('play', True)
        self.assertGreater(self.ai.action_preferences['play'], initial_pref)
    
    def test_learn_from_interaction_failure(self):
        """Test AI learns from failed interactions."""
        initial_pref = self.ai.action_preferences['play']
        self.ai.learn_from_interaction('play', False)
        self.assertLess(self.ai.action_preferences['play'], initial_pref)
    
    def test_analyze_interaction_pattern(self):
        """Test interaction pattern analysis."""
        self.pet.interaction_history = ['feed', 'play', 'feed', 'play', 'feed']
        stats = self.ai.analyze_interaction_pattern()
        self.assertEqual(stats['most_common'], 'feed')
        self.assertEqual(stats['total_interactions'], 5)
    
    def test_generate_response(self):
        """Test AI response generation."""
        response = self.ai.generate_response('play', True)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
    
    def test_predict_mood_change(self):
        """Test mood change prediction."""
        self.pet.hunger = 60.0
        mood_change = self.ai.predict_mood_change('feed')
        self.assertGreater(mood_change, 0)
    
    def test_to_dict(self):
        """Test converting AI to dictionary."""
        ai_dict = self.ai.to_dict()
        self.assertIn('action_preferences', ai_dict)
        self.assertIn('learning_rate', ai_dict)
    
    def test_from_dict(self):
        """Test creating AI from dictionary."""
        ai_dict = {
            'action_preferences': {'feed': 0.8, 'play': 0.6, 'train': 0.7, 'clean': 0.5, 'rest': 0.4},
            'learning_rate': 0.15
        }
        loaded_ai = PetAI.from_dict(self.pet, ai_dict)
        self.assertEqual(loaded_ai.action_preferences['feed'], 0.8)
        self.assertEqual(loaded_ai.learning_rate, 0.15)


class TestNLPProcessor(unittest.TestCase):
    """Test cases for the NLPProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.nlp = NLPProcessor()
    
    def test_parse_exact_command(self):
        """Test parsing exact command."""
        command, confidence = self.nlp.parse_command("feed")
        self.assertEqual(command, "feed")
        self.assertEqual(confidence, 1.0)
    
    def test_parse_natural_language(self):
        """Test parsing natural language input."""
        command, confidence = self.nlp.parse_command("I want to play with my pet")
        self.assertEqual(command, "play")
        self.assertGreater(confidence, 0.5)
    
    def test_parse_greeting(self):
        """Test parsing greetings."""
        command, confidence = self.nlp.parse_command("hello")
        self.assertEqual(command, "greeting")
    
    def test_parse_farewell(self):
        """Test parsing farewells."""
        command, confidence = self.nlp.parse_command("goodbye")
        self.assertEqual(command, "farewell")
    
    def test_parse_feed_variations(self):
        """Test various feed command formats."""
        variations = ["feed the pet", "give food", "hungry", "I want to feed"]
        for variation in variations:
            command, confidence = self.nlp.parse_command(variation)
            self.assertEqual(command, "feed")
    
    def test_parse_play_variations(self):
        """Test various play command formats."""
        variations = ["play", "let's have fun", "play with pet"]
        for variation in variations:
            command, confidence = self.nlp.parse_command(variation)
            self.assertEqual(command, "play")
    
    def test_generate_greeting(self):
        """Test greeting generation."""
        greeting = self.nlp.generate_greeting("TestPet", "happy")
        self.assertIsInstance(greeting, str)
        self.assertGreater(len(greeting), 0)
    
    def test_generate_farewell(self):
        """Test farewell generation."""
        farewell = self.nlp.generate_farewell("TestPet")
        self.assertIsInstance(farewell, str)
        self.assertGreater(len(farewell), 0)
    
    def test_generate_confusion_response(self):
        """Test confusion response generation."""
        response = self.nlp.generate_confusion_response("TestPet")
        self.assertIsInstance(response, str)
        self.assertIn("help", response.lower())
    
    def test_generate_talk_response(self):
        """Test talk response generation."""
        response = self.nlp.generate_talk_response(
            "TestPet",
            "happy",
            {'playfulness': 60, 'curiosity': 55}
        )
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
    
    def test_sentiment_analysis_positive(self):
        """Test positive sentiment detection."""
        sentiment = self.nlp.sentiment_analysis("I love playing with my pet, it's great!")
        self.assertEqual(sentiment, "positive")
    
    def test_sentiment_analysis_negative(self):
        """Test negative sentiment detection."""
        sentiment = self.nlp.sentiment_analysis("This is bad and terrible")
        self.assertEqual(sentiment, "negative")
    
    def test_sentiment_analysis_neutral(self):
        """Test neutral sentiment detection."""
        sentiment = self.nlp.sentiment_analysis("The pet is there")
        self.assertEqual(sentiment, "neutral")


class TestPersistence(unittest.TestCase):
    """Test cases for the PetPersistence class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = "test_pet_saves"
        self.persistence = PetPersistence(self.test_dir)
        self.pet = Pet("SaveTestPet")
        self.ai = PetAI(self.pet)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_save_directory_creation(self):
        """Test that save directory is created."""
        self.assertTrue(os.path.exists(self.test_dir))
    
    def test_save_pet(self):
        """Test saving a pet."""
        filepath = self.persistence.save_pet(self.pet, self.ai)
        self.assertTrue(os.path.exists(filepath))
    
    def test_load_pet(self):
        """Test loading a pet."""
        self.persistence.save_pet(self.pet, self.ai, "test_save")
        loaded_pet, loaded_ai = self.persistence.load_pet("test_save")
        
        self.assertEqual(loaded_pet.name, self.pet.name)
        self.assertEqual(loaded_pet.mood, self.pet.mood)
        self.assertIsNotNone(loaded_ai)
    
    def test_load_nonexistent_pet(self):
        """Test loading a nonexistent pet raises error."""
        with self.assertRaises(FileNotFoundError):
            self.persistence.load_pet("nonexistent")
    
    def test_list_saves(self):
        """Test listing save files."""
        self.persistence.save_pet(self.pet, self.ai, "save1")
        self.persistence.save_pet(self.pet, self.ai, "save2")
        
        saves = self.persistence.list_saves()
        self.assertIn("save1", saves)
        self.assertIn("save2", saves)
    
    def test_delete_save(self):
        """Test deleting a save file."""
        self.persistence.save_pet(self.pet, self.ai, "to_delete")
        self.assertTrue(self.persistence.save_exists("to_delete"))
        
        result = self.persistence.delete_save("to_delete")
        self.assertTrue(result)
        self.assertFalse(self.persistence.save_exists("to_delete"))
    
    def test_delete_nonexistent_save(self):
        """Test deleting nonexistent save returns False."""
        result = self.persistence.delete_save("nonexistent")
        self.assertFalse(result)
    
    def test_save_exists(self):
        """Test checking if save exists."""
        self.assertFalse(self.persistence.save_exists("test"))
        self.persistence.save_pet(self.pet, self.ai, "test")
        self.assertTrue(self.persistence.save_exists("test"))
    
    def test_get_save_info(self):
        """Test getting save file info."""
        self.persistence.save_pet(self.pet, self.ai, "info_test")
        info = self.persistence.get_save_info("info_test")
        
        self.assertIsNotNone(info)
        self.assertEqual(info['name'], self.pet.name)
        self.assertIn('experience', info)
        self.assertIn('mood', info)
    
    def test_get_nonexistent_save_info(self):
        """Test getting info for nonexistent save returns None."""
        info = self.persistence.get_save_info("nonexistent")
        self.assertIsNone(info)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete virtual pet system."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.pet = Pet("IntegrationPet")
        self.ai = PetAI(self.pet)
        self.nlp = NLPProcessor()
        self.test_dir = "test_integration_saves"
        self.persistence = PetPersistence(self.test_dir)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_complete_interaction_flow(self):
        """Test a complete interaction flow."""
        # Feed the pet
        success, message = self.pet.feed()
        self.assertTrue(success)
        self.ai.learn_from_interaction('feed', success)
        
        # Play with the pet
        self.pet.energy = 60.0
        success, message = self.pet.play()
        self.assertTrue(success)
        self.ai.learn_from_interaction('play', success)
        
        # Get AI suggestion
        action, reason = self.ai.get_suggested_action()
        self.assertIsNotNone(action)
        
        # Check stats
        stats = self.ai.analyze_interaction_pattern()
        self.assertGreater(stats['total_interactions'], 0)
    
    def test_nlp_to_action_flow(self):
        """Test NLP parsing to action execution."""
        # Parse natural language input
        command, confidence = self.nlp.parse_command("I want to feed my pet")
        self.assertEqual(command, "feed")
        
        # Execute the action
        self.pet.hunger = 50.0
        success, message = self.pet.feed()
        self.assertTrue(success)
    
    def test_save_and_load_flow(self):
        """Test saving and loading a pet with AI."""
        # Interact with pet
        self.pet.feed()
        self.pet.play()
        self.ai.learn_from_interaction('feed', True)
        
        # Save
        self.persistence.save_pet(self.pet, self.ai, "integration_test")
        
        # Load
        loaded_pet, loaded_ai = self.persistence.load_pet("integration_test")
        
        # Verify state is preserved
        self.assertEqual(loaded_pet.name, self.pet.name)
        self.assertEqual(len(loaded_pet.interaction_history), len(self.pet.interaction_history))
    
    def test_personality_adaptation_over_time(self):
        """Test that pet personality adapts through multiple interactions."""
        initial_playfulness = self.pet.personality['playfulness']
        
        # Multiple play sessions
        for _ in range(10):
            self.pet.energy = 60.0
            self.pet.play()
            self.ai.learn_from_interaction('play', True)
        
        # Personality should have increased
        self.assertGreater(self.pet.personality['playfulness'], initial_playfulness)
        
        # AI should prefer play more
        self.assertGreater(self.ai.action_preferences['play'], 0.5)


def run_tests():
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestPet))
    suite.addTests(loader.loadTestsFromTestCase(TestPetAI))
    suite.addTests(loader.loadTestsFromTestCase(TestNLPProcessor))
    suite.addTests(loader.loadTestsFromTestCase(TestPersistence))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
