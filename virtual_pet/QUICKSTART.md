# Virtual Pet Game - Quick Start Guide

## Getting Started in 3 Simple Steps

### 1. Launch the Game
```bash
cd sp-converter
python3 virtual_pet/cli.py
```

### 2. Create or Load Your Pet
When you first start, you'll be prompted to:
- **Create a new pet**: Choose a unique name for your companion
- **Load an existing pet**: Continue with a previously saved pet

### 3. Start Interacting!
Type commands to care for your pet. Try these:

**Basic Commands:**
```
feed    - Feed your pet when hungry
play    - Play to boost mood
train   - Train to gain experience
clean   - Keep your pet clean
rest    - Restore energy
```

**Information Commands:**
```
status  - View detailed stats
talk    - Chat with your pet
suggest - Get AI recommendation
stats   - View interaction history
```

**Game Management:**
```
save    - Save your pet
help    - Show all commands
quit    - Exit (remember to save!)
```

## Natural Language Support

You can also use natural language! Try:
- "I want to feed my pet"
- "Let's play!"
- "How is my pet doing?"
- "Give my pet a bath"

## Understanding Your Pet

### Status Indicators
- **Mood** (0-100%): Overall happiness
- **Health** (0-100%): Physical well-being
- **Energy** (0-100%): Activity level
- **Hunger** (0-100%): Need for food (higher = more hungry)
- **Cleanliness** (0-100%): Hygiene level
- **Experience**: Learning progress (XP)

### Personality Traits
Your pet develops these traits through interaction:
- **Playfulness**: Increases when you play
- **Curiosity**: Increases when you train
- **Independence**: Increases through training
- **Friendliness**: General social development

## Tips for Success

1. **Watch for AI suggestions** - Type `suggest` to get smart recommendations
2. **Check status regularly** - Type `status` to see what your pet needs
3. **Save often** - Type `save` to preserve your pet's progress
4. **Balance activities** - Mix feeding, playing, training, and rest
5. **Talk to your pet** - Use `talk` to see mood-based responses

## What Affects Your Pet?

### Time-Based Changes
Your pet's state changes naturally over time:
- Hunger increases
- Energy decreases
- Cleanliness decreases
- Mood affected by other stats

### Action Effects
- **Feed**: ↓ Hunger, ↑ Mood, small ↑ Energy
- **Play**: ↑↑ Mood, ↓ Energy, small ↑ Hunger, ↑ Playfulness
- **Train**: ↑↑ Experience, ↓ Energy, ↑ Hunger, ↑ Curiosity
- **Clean**: ↑↑ Cleanliness, ↑ Mood
- **Rest**: ↑↑ Energy, small ↑ Hunger

## Example Session

```
🎮 [Buddy] > status

🐾 Buddy's Status:
  Mood:        ██████████████ 70.0% (content)
  Health:      ████████████████████ 100.0%
  Energy:      ████████████ 60.0%
  Hunger:      ████████ 40.0%

🎮 [Buddy] > suggest

💡 AI Suggestion: feed
   Reason: Buddy is getting hungry.

🎮 [Buddy] > feed

Buddy enjoyed the meal! Hunger reduced significantly.
💭 Nom nom! Buddy is happy!

🎮 [Buddy] > play

Buddy had a great time playing! Mood improved but got a bit tired.
💭 Buddy loves playing with you!

🎮 [Buddy] > save
✅ Buddy has been saved
```

## Advanced Features

### AI Learning
- The AI learns which actions you prefer
- It adapts suggestions based on success/failure
- Tracks interaction patterns for insights

### Natural Language
- Supports varied command phrasings
- Recognizes greetings and farewells
- Context-aware dialogue generation

### Save System
- Automatic save location: `pet_saves/`
- Multiple save slots supported
- View save info before loading

## Troubleshooting

**Q: My pet won't do an action?**  
A: Check if your pet has the energy or if the action is needed. For example, you can't feed a full pet.

**Q: Where are my saves?**  
A: Saves are stored in the `pet_saves/` directory as JSON files.

**Q: How do I see my pet's personality?**  
A: Use the `status` command to see detailed stats including personality traits.

**Q: Can I have multiple pets?**  
A: Yes! Create different pets and use `save` with custom names, then `load` to switch between them.

## Demo Mode

Want to see it in action first? Run the demo:
```bash
python3 virtual_pet/demo.py
```

This shows a quick automated demo of all features.

## Having Fun!

Remember:
- 🐾 There's no "winning" - just enjoy caring for your pet
- 💡 Experiment with different interaction patterns
- 📊 Watch how personality develops over time
- 💾 Save regularly to preserve your pet's unique personality
- 😊 Have fun building a bond with your virtual companion!

---

For complete technical documentation, see [virtual_pet/README.md](README.md)
