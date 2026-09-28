import json

from pathlib import Path

class JSONObject:
    def __init__(self: JSONObject, data: list[dict] = [], filepath: Path | None = None) -> None:
        
        if filepath:
            self.data = self.load_json_from_file(filepath)
            return
        
        self.data = data
    
    def load_json_from_file(self: JSONObject, filepath: Path | None = None):
        if not filepath:
            raise ValueError("Filepath must be provided to load JSON from a file.")
        elif not filepath.exists():
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {filepath}: {e}")
        
    def validate_json(self: JSONObject, schema): # Returns a boolean
        # TODO: Implement JSON validation logic
        pass
    
class JSONParser:
    pass