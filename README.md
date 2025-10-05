# SP-Converter Repository

## Overview

This repository contains:

1. **SQL to C# Converter**: An AI-powered tool for converting SQL Server stored procedures to C# code using LLM and RAG (Retrieval-Augmented Generation) pipeline.

2. **Virtual Pet Game**: An AI-powered virtual pet game with intelligent behavior, natural language processing, and reinforcement learning.

## Installation

### SQL to C# Converter

1. Install dependencies:
```bash
pip install vllm transformers torch
```

### Virtual Pet Game

The virtual pet game has no external dependencies and uses only Python's standard library.

## Usage

### Virtual Pet Game

Run the interactive virtual pet game:
```bash
python3 virtual_pet/cli.py
```

Or run the quick demo:
```bash
python3 virtual_pet/demo.py
```

See [virtual_pet/README.md](virtual_pet/README.md) for complete documentation.

### Testing

Run the virtual pet test suite:
```bash
python3 tests/test_virtual_pet.py
```

## Features

### Virtual Pet Game
- 🐾 Interactive pet care (feed, play, train, clean, rest)
- 🤖 AI-driven behavior with reinforcement learning
- 💬 Natural language command processing
- 📊 Dynamic state management (mood, health, energy, etc.)
- 🎭 Personality development through interactions
- 💾 Save/load pet state between sessions
- ✅ Comprehensive test coverage (53 tests)

## Project Structure

```
.
├── src/                    # SQL to C# converter source
├── virtual_pet/           # Virtual pet game
│   ├── pet.py            # Core pet state management
│   ├── ai_behavior.py    # AI and learning logic
│   ├── nlp_processor.py  # Natural language processing
│   ├── persistence.py    # Save/load functionality
│   ├── cli.py           # Command-line interface
│   └── README.md        # Detailed documentation
├── tests/                # Test suite
└── README.md            # This file
```

## License

See repository license for details.
