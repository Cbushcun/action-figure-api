import json

from pathlib import Path

class JSONManager:
    "Project-specific JSON management class for centralized handling."
    def __init__(self: JSONManager) -> None:
        pass
    
    def load_file(self, filepath: str = "") -> list[dict] | None:
        """Loads JSON from given filepath. Returns JSON data or `None`."""
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            return None