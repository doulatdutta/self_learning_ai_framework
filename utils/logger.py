import logging
from config.settings import Settings

class Logger:
    def __init__(self, name="app_logger"):
        """
        Initializes the logger instance.

        :param name: Name of the logger.
        """
        settings = Settings()
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG if settings.debug_mode else logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # File handler
        file_handler = logging.FileHandler(settings.log_file)
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """
        Returns the configured logger instance.

        :return: Logger instance.
        """
        return self.logger
