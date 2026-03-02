import json


class DataManager:
    def __init__(self, FILENAME = "PYTHON BACK END/Day-07-Student-Backend/data/students.json"):
        self.FILENAME = FILENAME
    def load_data(self):
        try:
            with open(self.FILENAME, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    def save_data(self, data):
        with open(self.FILENAME, "w") as file:
            json.dump(data, file, indent = 4)

    