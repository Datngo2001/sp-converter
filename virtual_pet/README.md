# Virtual Pet Game - AI-Powered Companion

## Overview

An interactive virtual pet game built with Python that leverages AI techniques for intelligent pet behavior and natural language interaction. Users can care for their virtual pet through various activities while the pet learns and adapts to develop a unique personality over time.

## Features

### 🐾 Core Functionality
- **Interactive Pet Care**: Feed, play, train, clean, and rest with your virtual pet
- **Dynamic State Management**: Pet has mood, health, energy, hunger, and cleanliness that evolve over time
- **AI-Driven Behavior**: Pet uses rule-based logic and reinforcement learning to adapt to user interactions
- **Personality Development**: Pet develops unique personality traits (playfulness, friendliness, independence, curiosity) based on interactions
- **Natural Language Processing**: Communicate with your pet using natural language commands
- **Intelligent Suggestions**: AI recommends actions based on pet's current needs
- **State Persistence**: Save and load your pet's state between sessions

### 🎮 User Interface
- Command-line interface (CLI) with intuitive commands
- Natural language command processing
- Visual status bars for pet attributes
- Contextual responses based on pet's personality

## Technology Stack

- **Python 3.x**: Core programming language
- **AI/ML**: Custom reinforcement learning implementation for pet behavior adaptation
- **NLP**: Pattern matching and keyword-based natural language processing
- **Data Persistence**: JSON-based file storage
- **Testing**: unittest framework for comprehensive test coverage

## Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses Python standard library)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Datngo2001/sp-converter.git
cd sp-converter
```

2. The virtual pet game is self-contained in the `virtual_pet` directory with no additional dependencies needed.

## Usage

### Starting the Game

Run the game from the command line:

```bash
python3 virtual_pet/cli.py
```

Or using Python module syntax:

```bash
python3 -m virtual_pet.cli
```

### Creating or Loading a Pet

When you start the game, you'll be prompted to either:
1. Create a new pet (choose a name)
2. Load an existing saved pet

### Available Commands

#### Basic Actions
- `feed` - Feed your pet to reduce hunger
- `play` - Play with your pet to improve mood
- `train` - Train your pet to gain experience
- `clean` - Clean your pet to improve cleanliness
- `rest` - Let your pet rest to restore energy

#### Information & AI
- `status` - View detailed pet statistics
- `talk` - Have a conversation with your pet
- `suggest` - Get AI recommendation for next action
- `stats` - View interaction statistics

#### Game Management
- `save` - Save your pet's current state
- `load` - Load a different saved pet
- `help` - Display available commands
- `quit`/`exit` - Exit the game

### Natural Language Interaction

You can also use natural language phrases like:
- "I want to feed my pet"
- "Let's play"
- "How is my pet doing?"
- "Give the pet a bath"

## Architecture

### Module Structure

```
virtual_pet/
├── __init__.py          # Package initialization
├── pet.py              # Core Pet class with state management
├── ai_behavior.py      # AI behavior and learning logic
├── nlp_processor.py    # Natural language processing
├── persistence.py      # Save/load functionality
└── cli.py             # Command-line interface
```

### Core Components

#### Pet Class (`pet.py`)
Manages the pet's state and attributes:
- **Attributes**: mood, health, energy, hunger, cleanliness, experience
- **Personality Traits**: playfulness, friendliness, independence, curiosity
- **Actions**: feed(), play(), train(), clean(), rest()
- **State Updates**: Automatic decay of attributes over time

#### PetAI Class (`ai_behavior.py`)
Implements intelligent behavior:
- **Action Suggestions**: Rule-based recommendations based on pet needs
- **Reinforcement Learning**: Learns from successful/failed interactions
- **Response Generation**: Creates contextual responses based on personality
- **Pattern Analysis**: Tracks and analyzes interaction patterns

#### NLPProcessor Class (`nlp_processor.py`)
Handles natural language understanding:
- **Command Parsing**: Extracts intent from natural language input
- **Pattern Matching**: Regex-based command recognition
- **Dialogue Generation**: Creates contextual responses
- **Sentiment Analysis**: Basic sentiment detection

#### PetPersistence Class (`persistence.py`)
Manages save/load operations:
- **JSON Serialization**: Converts pet state to/from JSON
- **File Management**: Creates, loads, and deletes save files
- **Save Information**: Provides metadata about saved pets

## Game Mechanics

### Pet State System

Each pet has the following attributes (0-100 scale):

- **Mood**: Overall happiness level
  - Affected by hunger, energy, cleanliness, and health
  - Improves with play and care
  
- **Health**: Physical well-being
  - Decreases if hunger is too high or cleanliness too low
  - Maintained through proper care

- **Energy**: Activity level
  - Decreases with play, training, and over time
  - Restored through rest

- **Hunger**: Need for food (higher = more hungry)
  - Increases over time
  - Reduced by feeding

- **Cleanliness**: Hygiene level
  - Decreases over time
  - Improved by cleaning

- **Experience**: Learning progress
  - Gained through training
  - Tracks pet's development

### Personality Development

The pet develops four personality traits:

1. **Playfulness**: Increases with play interactions
2. **Friendliness**: Increases with general interactions
3. **Independence**: Increases with training
4. **Curiosity**: Increases with training and exploration

### AI Learning Mechanism

The AI uses a simple reinforcement learning approach:

1. **Action Preferences**: Each action has a preference score (0-1)
2. **Positive Reinforcement**: Successful actions increase preference
3. **Negative Reinforcement**: Failed actions slightly decrease preference
4. **Adaptive Behavior**: Pet gradually prefers actions that succeed more often

### Time-Based Changes

Pet attributes naturally change over time:
- Hunger increases (~0.5% per minute)
- Energy decreases (~0.3% per minute)
- Cleanliness decreases (~0.2% per minute)
- Mood affected by other attributes

## Testing

### Running Tests

Execute the comprehensive test suite:

```bash
python3 tests/test_virtual_pet.py
```

### Test Coverage

The test suite includes:
- **Pet State Tests**: Creation, actions, state updates, serialization
- **AI Behavior Tests**: Suggestions, learning, pattern analysis
- **NLP Tests**: Command parsing, dialogue generation, sentiment analysis
- **Persistence Tests**: Save/load operations, file management
- **Integration Tests**: Complete interaction flows, system-wide behavior

All tests use Python's unittest framework and achieve comprehensive coverage of core functionality.

## Examples

### Basic Interaction Session

```
🐾 VIRTUAL PET GAME - AI-Powered Companion 🐾

What would you like to name your pet? Buddy

✨ Buddy has been created!

🐾 Buddy's Status:
  Mood:        ██████████████ 70.0% (content)
  Health:      ████████████████████ 100.0%
  Energy:      ████████████████ 80.0%
  Hunger:      ██████ 30.0%
  Cleanliness: ██████████████████ 90.0%
  Experience:  0 XP

🎮 [Buddy] > play

Buddy had a great time playing! Mood improved but got a bit tired.
💭 Buddy loves playing with you!
   Mood: 85.0% | Energy: 57.3% | Hunger: 35.0%

🎮 [Buddy] > suggest

💡 AI Suggestion: feed
   Reason: Buddy is getting hungry.

🎮 [Buddy] > feed

Buddy enjoyed the meal! Hunger reduced significantly.
💭 Nom nom! Buddy is happy!
   Mood: 95.0% | Energy: 62.3% | Hunger: 2.1%

🎮 [Buddy] > save
✅ Buddy has been saved to pet_saves/buddy_save.json
```

### Natural Language Interaction

```
🎮 [Buddy] > I want to train my pet

Buddy learned something new! Gained 12 experience.
💭 Buddy is a quick learner!

🎮 [Buddy] > How is Buddy doing?

🐾 Buddy's Status:
  Mood:        ██████████████████ 92.0% (very happy)
  Health:      ████████████████████ 100.0%
  Energy:      ██████████ 52.0%
  Hunger:      ████ 18.0%
  ...

🎮 [Buddy] > talk

💬 Buddy: I'm having such a wonderful time with you!
```

## Code Documentation

All modules are thoroughly documented with:
- Module-level docstrings
- Class docstrings with attribute descriptions
- Method docstrings with parameter and return value descriptions
- Inline comments for complex logic

### Example Usage in Code

```python
from virtual_pet import Pet, PetAI, PetPersistence

# Create a new pet
pet = Pet("Fluffy")
ai = PetAI(pet)

# Interact with the pet
success, message = pet.play()
ai.learn_from_interaction('play', success)

# Get AI suggestion
action, reason = ai.get_suggested_action()
print(f"Suggestion: {action} - {reason}")

# Save the pet
persistence = PetPersistence()
persistence.save_pet(pet, ai)

# Load later
loaded_pet, loaded_ai = persistence.load_pet("fluffy_save")
```

## Design Decisions

### Why Rule-Based AI?
- **Simplicity**: Easy to understand and maintain
- **Predictability**: Consistent behavior patterns
- **No Dependencies**: No need for external ML libraries
- **Educational**: Clear demonstration of AI concepts

### Why JSON for Persistence?
- **Human-Readable**: Easy to inspect and debug
- **Standard Library**: No external dependencies
- **Portable**: Works across platforms
- **Simple**: Easy to implement and maintain

### Why CLI Interface?
- **Accessibility**: Works on any system with Python
- **Simplicity**: Focus on core game mechanics
- **No Dependencies**: No GUI framework needed
- **Extensible**: Easy to add GUI later if desired

## Future Enhancements

Potential improvements for future versions:

1. **Enhanced AI**: Neural network-based behavior prediction
2. **Advanced NLP**: Integration with spaCy or transformers for better dialogue
3. **GUI Interface**: tkinter or PyQt-based graphical interface
4. **Multiple Pets**: Support for managing multiple pets
5. **Mini-Games**: Interactive games to play with pet
6. **Achievements**: Unlock rewards for milestones
7. **Multiplayer**: Share pets or compete with friends
8. **Advanced Traits**: More complex personality system

## Contributing

Contributions are welcome! Please ensure:
- All tests pass
- New features include tests
- Code follows existing style
- Documentation is updated

## License

This project is part of the sp-converter repository.

## Acknowledgments

Built as part of the AI-powered Virtual Pet Game feature for the sp-converter project.
