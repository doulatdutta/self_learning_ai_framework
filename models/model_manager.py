import os
import pickle

class ModelManager:
    def __init__(self, model_storage_path="models/"):
        self.model_storage_path = model_storage_path
        self.models = {}
        if not os.path.exists(self.model_storage_path):
            os.makedirs(self.model_storage_path)

    def save_model(self, model, model_name):
        file_path = os.path.join(self.model_storage_path, f"{model_name}.pkl")
        with open(file_path, "wb") as model_file:
            pickle.dump(model, model_file)
        print(f"Model {model_name} has been saved.")

    def load_model(self, model_name):
        file_path = os.path.join(self.model_storage_path, f"{model_name}.pkl")
        if os.path.exists(file_path):
            with open(file_path, "rb") as model_file:
                model = pickle.load(model_file)
            print(f"Model {model_name} has been loaded.")
            self.models[model_name] = model
            return model
        else:
            print(f"Model {model_name} not found.")
            return None

    def register_model(self, model_name, model):
        self.models[model_name] = model
        print(f"Model {model_name} has been registered.")

    def get_model(self, model_name):
        return self.models.get(model_name)

    def train_model(self, model_name, training_data):
        model = self.get_model(model_name)
        if model:
            # Implement training logic here using training_data
            print(f"Training {model_name} with data: {training_data}")
            # Example: Assuming model has a fit method
            # model.fit(training_data)
            print(f"Training {model_name} completed.")  # Indicate completion
        else:
            raise ValueError(f"Model {model_name} not found.")

    def list_models(self):
        return [f for f in os.listdir(self.model_storage_path) if f.endswith(".pkl")]
