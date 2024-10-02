# frameworks/framework_creator.py

import os
from .framework_base import FrameworkBase

class FrameworkCreator:
    def __init__(self):
        self.base_dir = "frameworks"  # Change to your preferred base directory

    def create_framework(self, framework_name):
        framework_path = os.path.join(self.base_dir, framework_name)
        if not os.path.exists(framework_path):
            os.makedirs(framework_path)
            print(f"Framework '{framework_name}' created successfully.")

            # Create a default framework file (optional)
            with open(os.path.join(framework_path, f"{framework_name}.py"), 'w') as f:
                f.write(f"# {framework_name} Framework\n\n")
                f.write(f"from .framework_base import FrameworkBase\n\n")
                f.write(f"class {framework_name}(FrameworkBase):\n")
                f.write(f"    def __init__(self):\n")
                f.write(f"        super().__init__('{framework_name}')\n")
                f.write(f"\n")
                f.write(f"    def run(self):\n")
                f.write(f"        print(f'Running {self.name} framework...')\n")
                print(f"Default framework file created for '{framework_name}'.")
        else:
            print(f"Framework '{framework_name}' already exists.")

    def list_frameworks(self):
        return [d for d in os.listdir(self.base_dir) if os.path.isdir(os.path.join(self.base_dir, d))]
