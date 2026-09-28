import json
import os

class JSONObject:
    def __init__(self: JSONObject, data: list = [], filepath: str | None = None) -> None:
        self.data: list[dict] = []
        
        if filepath:
            self.data = self.load_json_from_file(filepath)
        else:
            # TODO: Validate that data is a valid JSON object (dict or list) or throw erorr.
            self.data = data
    
    def load_json_from_file(self: JSONObject, filepath: str | None = None):
        
        if not filepath:
            raise ValueError("Filepath must be provided to load JSON from a file.")
        elif not os.path.exists(filepath):
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        
        try:
            with open(filepath, 'r') as file:
                # TODO: Add error handling for JSON decoding errors.
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {filepath}: {e}")
        
    def validate_json(self: JSONObject, schema): # Returns a boolean
        # TODO: Implement JSON validation logic
        pass