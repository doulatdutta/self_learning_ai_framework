import json
import os

class DataManager:
    def __init__(self, data_path="data/"):
        """
        DataManager handles the storage and retrieval of data.

        :param data_path: Path to where data files are stored.
        """
        self.data_path = data_path
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)

    def save_data(self, data, filename):
        """
        Saves data to a JSON file.

        :param data: Data to be saved.
        :param filename: Name of the file (without extension).
        :return: None
        """
        file_path = os.path.join(self.data_path, f"{filename}.json")
        with open(file_path, "w") as data_file:
            json.dump(data, data_file)
        print(f"Data saved to {filename}.json.")

    def load_data(self, filename):
        """
        Loads data from a JSON file.

        :param filename: Name of the file (without extension).
        :return: The loaded data, or None if the file is not found.
        """
        file_path = os.path.join(self.data_path, f"{filename}.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as data_file:
                data = json.load(data_file)
            print(f"Data loaded from {filename}.json.")
            return data
        else:
            print(f"File {filename}.json not found.")
            return None
