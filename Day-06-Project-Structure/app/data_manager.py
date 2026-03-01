import json
import os

class DataManager:
    """
    Manages loading and saving data to a JSON file.
    This class is responsible for all file I/O operations.
    """
    def __init__(self, filename):
        self.filename = filename
        # Ensure the directory for the file exists, creating it if necessary.
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def load_data(self):
        """Loads data from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty/invalid, return an empty list
            return []

    def save_data(self, data):
        """Saves data to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
