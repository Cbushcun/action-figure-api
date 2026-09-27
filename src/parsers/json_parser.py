import json
import os

class JSONObject:
    def __init__(self, data=[], file_path=None):
        if file_path:
            self.data = self.load_json_from_file(file_path)
        else:
            # TODO: Validate that data is a valid JSON object (dict or list) or throw erorr.
            self.data = data
    
    def load_json_from_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        try:
            with open(file_path, 'r') as file:
                        # TODO: Add error handling for JSON decoding errors.
                        return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {file_path}: {e}")
        
    def validate_json(self, schema):
        # TODO: Implement JSON validation logic
        pass