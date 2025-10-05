# Virtual Pet Game - Example Session Output

This file shows what users will see when interacting with the virtual pet game.

## Starting the Game

```
$ python3 virtual_pet/cli.py

============================================================
      🐾 VIRTUAL PET GAME - AI-Powered Companion 🐾
============================================================

Would you like to:
  1. Create a new pet
  2. Load an existing pet

Enter your choice (1 or 2):
> 1

🐣 Let's create your new pet!
What would you like to name your pet? Buddy

✨ Buddy has been created!

🐾 Buddy's Status:
==================================================
  Mood:        ██████████████ 70.0% (content)
  Health:      ████████████████████ 100.0%
  Energy:      ████████████████ 80.0%
  Hunger:      ██████ 30.0%
  Cleanliness: ██████████████████ 90.0%
  Experience:  0 XP


📋 Available Commands:
  feed      - Feed your pet
  play      - Play with your pet
  train     - Train your pet
  clean     - Clean your pet
  rest      - Let your pet rest
  talk      - Talk to your pet
  status    - Check pet's status
  suggest   - Get AI suggestion for next action
  stats     - View interaction statistics
  save      - Save your pet
  load      - Load a saved pet
  help      - Show this help message
  quit/exit - Exit the game


💬 You can type commands or talk naturally to your pet!
   (Type 'help' anytime to see available commands)

🎮 [Buddy] > 
```

## Example Interactions

### Feeding the Pet

```
🎮 [Buddy] > I want to feed my pet

Buddy enjoyed the meal! Hunger reduced significantly.
💭 Nom nom! Buddy is happy!
   Mood: 80.0% | Energy: 85.0% | Hunger: 5.2%

🎮 [Buddy] > 
```

### Playing with the Pet

```
🎮 [Buddy] > play

Buddy had a great time playing! Mood improved but got a bit tired.
💭 Buddy loves playing with you!
   Mood: 95.0% | Energy: 62.3% | Hunger: 10.0%

🎮 [Buddy] > 
```

### Getting AI Suggestions

```
🎮 [Buddy] > suggest

💡 AI Suggestion: rest
   Reason: Buddy could use some rest.
   Expected mood change: +10%

🎮 [Buddy] > 
```

### Training the Pet

```
🎮 [Buddy] > train

Buddy learned something new! Gained 12 experience.
💭 Buddy is a quick learner!
   Mood: 98.5% | Energy: 38.1% | Hunger: 20.0%

🎮 [Buddy] > 
```

### Checking Status

```
🎮 [Buddy] > status

🐾 Buddy's Status:
==================================================
  Mood:        ███████████████████ 98.5% (very happy)
  Health:      ████████████████████ 100.0%
  Energy:      ███████ 38.1%
  Hunger:      ████ 20.0%
  Cleanliness: ████████████████ 85.3%
  Experience:  12 XP

🎭 Personality Traits:
  Playfulness     ███████████ 53.5%
  Friendliness    ██████████ 50.0%
  Independence    ██████████ 51.2%
  Curiosity       ███████████ 52.8%

🎮 [Buddy] > 
```

### Talking to the Pet

```
🎮 [Buddy] > talk

💬 Buddy: I'm having such a wonderful time with you!

🎮 [Buddy] > 
```

### Viewing Statistics

```
🎮 [Buddy] > stats

📊 Interaction Statistics:
  Total interactions: 5
  Most common action: play (2 times)

  Action distribution:
    feed: 1 times
    play: 2 times
    train: 1 times
    rest: 1 times

🎮 [Buddy] > 
```

### Natural Language Examples

```
🎮 [Buddy] > hello there!

Hello! Buddy is very happy to see you!

🎮 [Buddy] > how is Buddy doing?

🐾 Buddy's Status:
==================================================
  Mood:        ███████████████████ 95.0% (very happy)
  Health:      ████████████████████ 100.0%
  Energy:      ████████████ 62.0%
  ...

🎮 [Buddy] > let's have some fun

Buddy had a great time playing! Mood improved but got a bit tired.
💭 Buddy is having so much fun!
   Mood: 100.0% | Energy: 45.7% | Hunger: 15.0%

🎮 [Buddy] > 
```

### Saving and Exiting

```
🎮 [Buddy] > save

✅ Buddy has been saved to pet_saves/buddy_save.json

🎮 [Buddy] > goodbye

Goodbye! Buddy will miss you!

💾 Don't forget to save your pet before leaving!
Would you like to save now? (yes/no): yes
✅ Buddy has been saved to pet_saves/buddy_save.json

✨ Thanks for playing! Come back soon! ✨
```

## Loading a Saved Pet

```
$ python3 virtual_pet/cli.py

============================================================
      🐾 VIRTUAL PET GAME - AI-Powered Companion 🐾
============================================================

Would you like to:
  1. Create a new pet
  2. Load an existing pet

Enter your choice (1 or 2):
> 2

📂 Available Saves:
  1. Buddy - XP: 12, Mood: 100.0%

Enter the number or name of the save to load (or 'cancel' to go back):
> 1

✅ Loaded Buddy!

🐾 Buddy's Status:
==================================================
  Mood:        ████████████████████ 100.0% (very happy)
  Health:      ████████████████████ 100.0%
  Energy:      █████████ 45.7%
  Hunger:      ███ 15.0%
  Cleanliness: ███████████████ 82.1%
  Experience:  12 XP

🎮 [Buddy] > 
```

## Demo Mode

```
$ python3 virtual_pet/demo.py

============================================================
   VIRTUAL PET GAME - Quick Demo
============================================================

Creating a new pet named 'Demo'...

📊 Initial Status:
  mood: 70.0
  health: 100.0
  energy: 80.0
  hunger: 30.0
  cleanliness: 90.0
  experience: 0

🎮 Performing actions...

1. Feeding Demo...
   Demo enjoyed the meal! Hunger reduced significantly.

2. Playing with Demo...
   Demo had a great time playing! Mood improved but got a bit tired.
   Demo enjoyed that.

3. Training Demo...
   Demo learned something new! Gained 13 experience.

💡 AI Suggestion:
   Action: rest
   Reason: Demo could use some rest.

📈 Interaction Statistics:
   Total interactions: 3
   Most common: feed

💬 Testing NLP:
   'I want to feed my pet' -> feed (confidence: 0.80)
   'let's play!' -> play (confidence: 0.80)
   'how is Demo doing?' -> status (confidence: 0.80)
   'hello' -> greeting (confidence: 0.90)

💾 Testing Persistence:
   Saved to: demo_saves/demo_test.json
   Loaded pet: Demo
   Experience: 13

📊 Final Status:
  Mood: 95.0% (very happy)
  Health: 100.0%
  Energy: 31.5%
  Hunger: 32.0%
  Experience: 13 XP

  Personality:
    playfulness: 50.5
    friendliness: 50.0
    independence: 50.3
    curiosity: 50.4

✅ Demo completed successfully!
============================================================
```

## Test Output

```
$ python3 tests/test_virtual_pet.py

test_clean_action (__main__.TestPet.test_clean_action)
Test cleaning the pet. ... ok
test_feed_action (__main__.TestPet.test_feed_action)
Test feeding the pet. ... ok
... [48 more tests] ...
test_save_and_load_flow (__main__.TestIntegration.test_save_and_load_flow)
Test saving and loading a pet with AI. ... ok

----------------------------------------------------------------------
Ran 53 tests in 0.008s

OK
```

---

**Note**: All emoji, colors, and formatting are displayed in the actual terminal for an engaging user experience!
