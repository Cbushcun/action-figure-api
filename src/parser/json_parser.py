import json

from pathlib import Path

class JSONParser:
    def __init__(self: JSONParser) -> None:
        self._content: list[dict[str, object]] = []
    
    def parse_from_file(self: JSONParser, filepath: Path) -> list[dict]:
        if not filepath.exists():
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        
        try:
            with open(filepath, 'r') as file:
                self._content = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {filepath}: {e}")    
        
        return self._content