"""
Persistence module for saving and loading pet state.
Uses JSON for simple file-based storage.
"""

import json
import os
from typing import Optional
from pathlib import Path


class PetPersistence:
    """
    Handles saving and loading pet state to/from JSON files.
    """
    
    def __init__(self, save_directory: str = "pet_saves"):
        """
        Initialize persistence handler.
        
        Args:
            save_directory: Directory to store save files
        """
        self.save_directory = Path(save_directory)
        self.save_directory.mkdir(parents=True, exist_ok=True)
    
    def save_pet(self, pet, ai=None, filename: Optional[str] = None) -> str:
        """
        Save pet state to a JSON file.
        
        Args:
            pet: Pet instance to save
            ai: Optional PetAI instance to save
            filename: Optional custom filename (without extension)
        
        Returns:
            Path to the saved file
        """
        if filename is None:
            filename = f"{pet.name.lower()}_save"
        
        filepath = self.save_directory / f"{filename}.json"
        
        save_data = {
            'pet': pet.to_dict(),
            'ai': ai.to_dict() if ai else None
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, indent=2)
        
        return str(filepath)
    
    def load_pet(self, filename: str):
        """
        Load pet state from a JSON file.
        
        Args:
            filename: Name of the save file (with or without .json extension)
        
        Returns:
            Tuple of (Pet, PetAI) or (Pet, None) if AI data not found
        
        Raises:
            FileNotFoundError: If save file doesn't exist
        """
        from virtual_pet.pet import Pet
        from virtual_pet.ai_behavior import PetAI
        
        if not filename.endswith('.json'):
            filename = f"{filename}.json"
        
        filepath = self.save_directory / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"Save file not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            save_data = json.load(f)
        
        pet = Pet.from_dict(save_data['pet'])
        
        ai = None
        if save_data.get('ai'):
            ai = PetAI.from_dict(pet, save_data['ai'])
        else:
            ai = PetAI(pet)
        
        return pet, ai
    
    def list_saves(self) -> list:
        """
        List all available save files.
        
        Returns:
            List of save file names (without extension)
        """
        saves = []
        for file in self.save_directory.glob("*.json"):
            saves.append(file.stem)
        return sorted(saves)
    
    def delete_save(self, filename: str) -> bool:
        """
        Delete a save file.
        
        Args:
            filename: Name of the save file to delete
        
        Returns:
            True if file was deleted, False if file didn't exist
        """
        if not filename.endswith('.json'):
            filename = f"{filename}.json"
        
        filepath = self.save_directory / filename
        
        if filepath.exists():
            filepath.unlink()
            return True
        return False
    
    def save_exists(self, filename: str) -> bool:
        """
        Check if a save file exists.
        
        Args:
            filename: Name of the save file to check
        
        Returns:
            True if file exists, False otherwise
        """
        if not filename.endswith('.json'):
            filename = f"{filename}.json"
        
        filepath = self.save_directory / filename
        return filepath.exists()
    
    def get_save_info(self, filename: str) -> Optional[dict]:
        """
        Get basic information about a save file without fully loading it.
        
        Args:
            filename: Name of the save file
        
        Returns:
            Dictionary with save info or None if file doesn't exist
        """
        if not filename.endswith('.json'):
            filename = f"{filename}.json"
        
        filepath = self.save_directory / filename
        
        if not filepath.exists():
            return None
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            pet_data = save_data.get('pet', {})
            return {
                'name': pet_data.get('name', 'Unknown'),
                'experience': pet_data.get('experience', 0),
                'mood': round(pet_data.get('mood', 0), 1),
                'health': round(pet_data.get('health', 0), 1),
                'file_size': filepath.stat().st_size,
                'modified': filepath.stat().st_mtime
            }
        except (json.JSONDecodeError, KeyError):
            return None
