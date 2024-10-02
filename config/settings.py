# config/settings.py

import os

# Define the path for the code folder
CODE_FOLDER = "D:\\buisness\\AI\\self_learning_ai_framework"

class Settings:
    def __init__(self):
        """
        Initializes the default settings for the application.
        """
        self.debug_mode = True
        self.database_file = "data/database.db"
        self.model_storage_path = "models/"
        self.log_file = "logs/app.log"
        self.api_timeout = 60  # in seconds
        self.code_folder = CODE_FOLDER  # Set the code folder path

    def get(self, setting_name):
        """
        Get the value of a specific setting.

        :param setting_name: The name of the setting to retrieve.
        :return: The value of the setting.
        """
        return getattr(self, setting_name, None)
