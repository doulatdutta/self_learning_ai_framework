# frameworks/framework_base.py

class FrameworkBase:
    def __init__(self, name):
        self.name = name

    def run(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def info(self):
        return f"Framework Name: {self.name}"
