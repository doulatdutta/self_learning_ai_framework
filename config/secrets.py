
from dotenv import load_dotenv
import os

class Secrets:
    def __init__(self):
        """
        Load sensitive information such as API keys, credentials, etc., from a .env file or environment variables.
        """
        # Load environment variables from .env file
        load_dotenv()

        # Retrieve sensitive information from environment variables
        self.api_key = os.getenv("OPENAI_API_KEY", "default_api_key")  # Replace with your key name
        self.db_password = os.getenv("DB_PASSWORD", "default_password")

    def get_secret(self, key_name):
        """
        Retrieves a secret value by its key name.

        :param key_name: The name of the secret to retrieve.
        :return: The secret value.
        """
        return getattr(self, key_name, None)

