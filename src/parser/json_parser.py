import json

from pathlib import Path

class JSONObject:
    def __init__(self: JSONObject) -> None:
        pass
    
        
    
class JSONParser:
    def __init__(self: JSONParser) -> None:
        pass
    
    def parse_from_file(self: JSONParser, filepath: Path) -> None:
        if not filepath.exists():
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        
        try:
            with open(filepath, 'r') as file:
                content: list[dict[str, object]] = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {filepath}: {e}")    
        
        pass